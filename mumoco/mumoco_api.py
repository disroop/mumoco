import json
from pathlib import Path
from typing import List

import cli_ui as ui
import deserialize
from conans.client.conan_api import Conan

from .conanbuilder.configreader import ConfigReader
from .conanbuilder.package import Package
from .conanbuilder.runner import Runner
from .conanbuilder.signature import Signature


class MumocoAPI:
    def __init__(self, config_file_path: str, root: str):
        self.config: ConfigReader = config_reader_from_file(config_file_path)
        self.runner: Runner = get_runner(self.config, root)

    def sources(self, source_folder: str = "") -> None:
        self.runner.get_all_sources(source_folder)

    def add_remotes(self, username: str, password: str) -> None:
        self.runner.add_all_remotes(self.config.remotes, username, password)

    def remove(self, source_folder: str = "") -> None:
        self.runner.remove_all_sources(source_folder)

    def create(self) -> None:
        self.runner.export_all()
        self.runner.create_all(self.config.configurations)

    def upload(self, remote_name: str) -> None:
        self.runner.upload_all_packages(remote_name)


def find_all_conanfiles_to_be_processed(root_path: str) -> List[str]:
    conan_files = []
    for path in Path(root_path).rglob("conanfile.py"):
        path_string = str(path.absolute())
        if "test_package" not in path_string:
            conan_files.append(path_string)
    return conan_files


def find_all_packages_to_processed(conan_factory: Conan, root_path: str, signature: Signature) -> List[Package]:
    conan_files = find_all_conanfiles_to_be_processed(root_path)

    conan_packages = []
    for file in conan_files:
        conan_packages.append(Package(conan_factory, signature, file))
    return conan_packages


def get_runner(config_reader: ConfigReader, root: str) -> Runner:
    conan_factory, _, _ = Conan.factory()
    packages = find_all_packages_to_processed(conan_factory, root, config_reader.signature)
    return Runner(conan_factory, packages)


def config_reader_from_file(file: str) -> ConfigReader:
    try:
        with open(file, encoding="utf-8") as json_file:
            return config_reader_from_string(json.load(json_file))
    except IOError:
        ui.fatal("Config file not accessible or readable")
    return ConfigReader()


def config_reader_from_string(load: str) -> ConfigReader:
    reader: ConfigReader = deserialize.deserialize(ConfigReader, load)
    return reader
