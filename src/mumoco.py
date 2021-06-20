import json
import sys
from pathlib import Path
from typing import List

import deserialize
from conans.client.conan_api import Conan

from src.conanbuilder.configreader import ConfigReader
from src.conanbuilder.package import Package
from src.conanbuilder.runner import Runner
from src.conanbuilder.signature import Signature

# pylint: disable=R0913
from src.exceptions import MumocoInvalidCommand

# pylint: disable=R0913
from src.exceptions import MumocoInvalidCommand


def mumoco_api(
    upload: str = "",
    remove: bool = False,
    create: bool = False,
    remotes: bool = False,
    sources: bool = False,
    username: str = "",
    password: str = "",
    root: str = "",  # maybe impove to use file path type
    config_file_path: str = "",  # maybe impove to use file path type
) -> None:
    if not (remotes or sources or remove or create or upload):
        raise MumocoInvalidCommand(
            """At least one execution command has to be set. Execution commands:
            + --remotes
            + --sources
            + --remove
            + --create
            + --upload"""
        )

    config = config_reader_from_file(config_file_path)
    runner = get_runner(config, root)
    if remotes:
        runner.add_all_remotes(config.remotes, username, password)
    if sources:
        runner.get_all_sources()
    if remove:
        runner.remove_all_sources()
    if create:
        runner.export_all()
        runner.create_all(config.configurations)
    if upload:
        runner.upload_all_packages(upload)


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
        with open(file) as json_file:
            return config_reader_from_string(json.load(json_file))
    except IOError:
        print("Config file not accessible or readable")
        sys.exit(1)


def config_reader_from_string(load: str) -> ConfigReader:
    reader: ConfigReader = deserialize.deserialize(ConfigReader, load)
    return reader
