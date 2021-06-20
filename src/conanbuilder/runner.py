"""
A runner
"""
from typing import List

from conans.client.conan_api import Conan

from .buildersettings import BuilderSettings
from .package import Package
from .remote import Remote


class Runner:
    def __init__(self, conan_factory: Conan, packages: List[Package]):
        self.conan_factory = conan_factory
        self.packages = packages

    def create_all(self, configurations: List[BuilderSettings], verbose: bool = True) -> None:
        if verbose:
            print("#######################################\n")
            print("########### create packages ###########\n")
            print("#######################################\n")

        for package in self.packages:
            package.create_for_all_configurations(configurations, verbose)

    # relative_path = path.absolute()
    # eprint(package.pattern)

    # package_signature = get_package_signature()
    # package_pattern=f'{package_signature.name}/{package_signature.version}
    # @{package_signature.user}/{package_signature.channel}'
    # conan_command_line.create(package.path,test_build_folder=f'/tmp/{package.pattern}/tbf')
    # TODO:profiles_names =HOST, profiles_build=build
    # conan_command_line.authenticate()
    # conan_command_line.remote_add()
    # conan_command_line.upload(package_pattern)
    # print(f'SUCCESS: {package_pattern}')
    def add_all_remotes(self, remotes: List[Remote], username: str, password: str, verbose: bool = True) -> None:
        if verbose:
            print(
                "#######################################\n"
                "########### add remote ################\n"
                "#######################################\n"
            )
        if remotes:
            for remote in remotes:
                self.add_remote(remote, username, password)
        else:
            raise Warning("No Remotes defined. Nothing to add!")

    def add_remote(self, remote: Remote, username: str, password: str) -> None:
        self.conan_factory.remote_add(
            remote_name=remote.name,
            url=remote.url,
            verify_ssl=remote.verify_ssl,
            insert=remote.priority,
            force=remote.force,
        )
        if remote.login:
            if not username or not password:
                raise Warning(f"Can't login to {remote.name} no username or password provided!")
            self.conan_factory.authenticate(name=username, password=password, remote_name=remote.name)

    def export_all(self, verbose: bool = True) -> None:
        if verbose:
            print(
                "#######################################\n"
                "###########    export all    ##########\n"
                "#######################################\n"
            )
        for package in self.packages:
            package.export()

    def get_all_sources(self, verbose: bool = True) -> None:
        if verbose:
            print(
                "#######################################\n"
                "########### download sources ##########\n"
                "#######################################\n"
            )
        for package in self.packages:
            package.source()

    def remove_all_sources(self, verbose: bool = True) -> None:
        if verbose:
            print(
                "#######################################\n"
                "########### remove sources ############\n"
                "#######################################\n"
            )
        for package in self.packages:
            package.source_remove()

    def upload_all_packages(self, remote: str, verbose: bool = True) -> None:
        if verbose:
            print(
                "#######################################\n"
                "########### upload packages ###########\n"
                "#######################################\n"
            )
        for package in self.packages:
            package.upload_package(remote)
