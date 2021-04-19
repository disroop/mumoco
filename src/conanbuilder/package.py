import copy
import shutil

from conans.client.conan_api import Conan, ProfileData

from .buildersettings import BuilderSettings
from .signature import Signature
from conans.errors import ConanException

class Package:
    source_folder = "tmp"

    def __init__(self, conanfactory, signature=Signature(), path='.'):
        self.conanfactory = conanfactory
        if ".py" not in path:
            path = f'{path}/conanfile.py'
        self.name = ""
        self._signature = copy.copy(signature)
        self._read_package_attributes(path)
        self.path = str(path).replace("conanfile.py", "")

    def get_path(self):
        return self.path

    def get_pattern(self):
        return f"{self.name}/{self._signature.version}@{self._signature.user}/{self._signature.channel}"

    def _get_attribute(self, path, attribute, fail_on_invalid=False):
        attribute = str(attribute)
        try:
            conan_package = self.conanfactory.inspect(path=f'{path}', attributes=[f'{attribute}'])
            return conan_package.get(attribute)
        except ConanException:
            if fail_on_invalid:
                raise Exception(f"Attribute not found: {attribute} in {path} - {ConanException}")
        return ""

    def _read_package_attributes(self, path):
        self.name = self._get_attribute(path, 'name', True)
        version = self._get_attribute(path, 'version')
        if version != "":
            self._signature.version = version
        user = self._get_attribute(path, 'user')
        if user != "":
            self._signature.user = user
        channel = self._get_attribute(path, 'channel')
        if channel != "":
            self._signature.channel = channel

    def _check_includes(self, includes):
        if len(includes) > 0:
            for include in includes:
                if include in self.path:
                    return True
            return False
        return True

    def is_withing_scope(self, configuration=BuilderSettings()):
        if not self._check_includes(configuration.includes):
            return False
        for exclude in configuration.excludes:
            if exclude in self.path:
                return False
        return True

    def export(self):
        self.conanfactory.export(self.path,
                                  self.name,
                                  self._signature.version,
                                  self._signature.user,
                                  self._signature.channel)

    def create(self, configuration=BuilderSettings()):
        pattern=self.get_pattern() 
        profile_build = ProfileData(profiles=[f"{configuration.build_profile}"],settings=configuration.convert_build_settings_str(),
                                    options="", env="")
        self.conanfactory.create(self.path,
                                  name=self.name,
                                  version=self._signature.version,
                                  user=self._signature.user,
                                  channel=self._signature.channel,
                                  profile_names=[f"{configuration.host_profile}"],
                                  profile_build=profile_build,
                                  settings=configuration.host_settings,
                                  build_modes=[f"{configuration.build}"],
                                  test_build_folder=f'/tmp/{pattern}/tbf')

    def source(self):
        self.conanfactory.source(self.path,
                                  source_folder=f"{self.path}/{self.source_folder}")

    def source_remove(self):
        shutil.rmtree(f"{self.path}/{self.source_folder}", ignore_errors=False, onerror=None);

    def upload_package(self, remote):
        pattern=self.get_pattern()
        self.conanfactory.upload(pattern,package=None,remote_name=remote)
