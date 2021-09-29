"""
The package class
"""
import copy
import shutil
import tempfile
from typing import List

import cli_ui as ui
from conans.client.conan_api import Conan, ProfileData
from conans.errors import ConanException

from .buildersettings import BuilderSettings
from .signature import Signature


class Package:
    def __init__(self, conan_factory: Conan, signature: Signature, path: str):
        self.conan_factory = conan_factory
        if ".py" not in path:
            path = f"{path}/conanfile.py"
        self.name = ""
        self._signature = copy.copy(signature)
        self._read_package_attributes(path)
        self.path: str = str(path).replace("conanfile.py", "")
        self.pattern = f"{self.name}/{self._signature.version}@{self._signature.user}/{self._signature.channel}"

    def _get_attribute(self, path: str, attribute: str, fail_on_invalid: bool = False) -> str:
        try:
            conan_package = self.conan_factory.inspect(path=f"{path}", attributes=[f"{attribute}"])
            return str(conan_package.get(attribute, ""))
        except ConanException:
            if fail_on_invalid:
                raise Exception(f"Attribute not found: {attribute} in {path} - {ConanException}") from ConanException
        return ""

    def _read_attribute(self, path: str, attribute_name: str, member: str, fail_on_invalid: bool) -> str:
        temp = self._get_attribute(path, attribute_name, fail_on_invalid)
        if fail_on_invalid:
            return temp
        if temp != "":
            return temp
        return member

    def _read_package_attributes(self, path: str) -> None:
        self.name = self._read_attribute(path, "name", self.name, True)
        self._signature.version = self._read_attribute(path, "version", self._signature.version, False)
        self._signature.user = self._read_attribute(path, "user", self._signature.user, False)
        self._signature.channel = self._read_attribute(path, "channel", self._signature.channel, False)

    def _is_path_in_includes(self, includes: List[str]) -> bool:
        if len(includes) > 0:
            for include in includes:
                if include in self.path:
                    return True
            return False
        return True

    def _is_path_in_excludes(self, excludes: List[str]) -> bool:
        for exclude in excludes:
            if exclude in self.path:
                return True
        return False

    def is_within_scope(self, configuration: BuilderSettings = BuilderSettings()) -> bool:
        if not self._is_path_in_includes(configuration.includes):
            return False
        return not self._is_path_in_excludes(configuration.excludes)

    def source_folder(self, base_folder: str = "") -> str:
        if base_folder:
            return f"{base_folder}/{self.name}"
        return f"{self.path}/tmp"

    def export(self) -> None:
        self.conan_factory.export(
            self.path, self.name, self._signature.version, self._signature.user, self._signature.channel
        )

    def create_for_all_configurations(self, configurations: List[BuilderSettings]) -> None:
        for configuration in configurations:
            self.create_for_configuration(configuration)

    def create_for_configuration(self, configuration: BuilderSettings) -> None:
        if not self.is_within_scope(configuration):
            return
        ui.info(ui.tabs(2), configuration)
        self.__create(configuration)

    def __create(self, configuration: BuilderSettings = BuilderSettings()) -> None:
        profile_build = ProfileData(
            profiles=[f"{configuration.build_profile}"],
            settings=configuration.build_settings,
            options="",
            env=None,
            conf=None,
        )
        self.conan_factory.create(
            self.path,
            name=self.name,
            version=self._signature.version,
            user=self._signature.user,
            channel=self._signature.channel,
            profile_names=[f"{configuration.host_profile}"],
            profile_build=profile_build,
            settings=configuration.host_settings,
            build_modes=[f"{configuration.build}"],
            test_build_folder=f"{tempfile.gettempdir()}/{self.pattern}/tbf",
        )

    def source(self, base_folder: str) -> None:
        self.conan_factory.source(self.path, source_folder=self.source_folder(base_folder))

    def source_remove(self, base_folder: str) -> None:
        shutil.rmtree(self.source_folder(base_folder), ignore_errors=False, onerror=None)

    def upload_package(self, remote_name: str) -> None:
        self.conan_factory.upload(self.pattern, package=None, remote_name=remote_name)
