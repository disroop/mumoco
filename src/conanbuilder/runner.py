from .signature import Signature
from .package import Package
from pathlib import Path
from conans.client.conan_api import Conan


class Runner:

    def __init__(self, root_path, signature=Signature()):
        self.conanfactory, _, _ = Conan.factory()
        self.packages = self._get_all_packages(root_path, signature)

    def create_all(self, configurations):
        for config in configurations:
            print("#######################################\n"
                  "########### create packages ###########\n"
                  f"# host profile:  {config.host_profile}\n"
                  f"# build profile: {config.build_profile}\n"
                  f"# host settings: {config.host_settings}\n"
                  f"# build settings: {config.build_settings}\n"
                  f"# build :         {config.build}\n"
                  f"# includes:      {config.includes}\n"
                  f"# excludes:      {config.excludes}\n"
                  "#######################################\n")
            for package in self.packages:
                if package.is_withing_scope(config):
                    package.create(config)

    # relative_path = path.absolute()
    # eprint(package.pattern)

    # package_signature = get_package_signature()
    # package_pattern=f'{package_signature.name}/{package_signature.version}@{package_signature.user}/{package_signature.channel}'
    # conan_command_line.create(package.path,test_build_folder=f'/tmp/{package.pattern}/tbf')
    # TODO:profiles_names =HOST, profiles_build=build
    # conan_command_line.authenticate()
    # conan_command_line.remote_add()
    # conan_command_line.upload(package_pattern)
    # print(f'SUCCESS: {package_pattern}')
    def add_all_remotes(self, remotes, username=None, password=None):
        print(
            "#######################################\n"
            "########### add remote ##########\n"
            "#######################################\n")
        if remotes:
            for remote in remotes:
                self.conanfactory.remote_add(remote_name=remote.name, url=remote.url, verify_ssl=remote.verify_ssl, insert=remote.priority, force=remote.force)
                if remote.login:
                    if not username or not password:
                        raise Warning(f"Can't login to {remote.name} no username or password provided!")
                    else:
                        self.conanfactory.authenticate(name=username, password=password, remote_name=remote.name)
        else:
            raise Warning("No Remotes defined. Nothing to add!")

    def _get_all_packages(self, root_path, signature=Signature()) -> object:
        conan_packages = []
        for path in Path(root_path).rglob('conanfile.py'):
            path = str(path.absolute())
            if "test_package" not in path:
                conan_packages.append(Package(self.conanfactory, signature, path))
        return conan_packages

    def export_all(self):
        for package in self.packages:
            package.export()

    def get_all_sources(self):
        print(
            "#######################################\n"
            "########### download sources ##########\n"
            "#######################################\n")
        for package in self.packages:
            package.source()

    def remove_all_sources(self):
        text = ()
        print("#######################################\n"
              "########### remove sources ############\n"
              "#######################################\n")
        for package in self.packages:
            package.source_remove()

    def upload_all_packages(self, remote):
        print("#######################################\n"
              "########### upload packages ###########\n"
              "#######################################\n")        
        for package in self.packages:
            package.upload_package(remote)
        