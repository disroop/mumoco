#!/usr/bin/python
"""
mumoco or multi module conan helps working with multiple conan package simultaneously.
"""
import argparse
import json
import os
import sys

import deserialize

from src.conanbuilder.configreader import ConfigReader
from src.conanbuilder.runner import Runner


def valid_args(args: argparse.Namespace) -> bool:
    if args.remotes or args.sources or args.remove or args.create or args.upload:
        return True
    return False


def get_args() -> argparse.Namespace:
    cwd = os.getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root", type=str, required=False, default=cwd, help="Path to root folder of multipackage module"
    )
    parser.add_argument(
        "--config", type=str, required=False, default=f"{cwd}/config-build.json", help="Path to config-build.json"
    )
    parser.add_argument("--username", type=str, required=False, default=None, help="User credentials")
    parser.add_argument("--password", type=str, required=False, default=None, help="Access token")
    parser.add_argument("--remotes", action="store_true", required=False, help="Add all remotes from config-build.json")
    parser.add_argument("--sources", action="store_true", required=False, help="Download sources to PACKAGE-PATH/tmp")
    parser.add_argument("--remove", action="store_true", required=False, help="Remove all sources")
    parser.add_argument("--create", action="store_true", required=False, help="Create all packages")
    parser.add_argument("--upload", type=str, required=False, help="Upload all packages to repository")
    args = parser.parse_args()
    if not valid_args(args):
        print(
            """At least one execution command has to be set. Execution commands:
        + --remotes
        + --sources
        + --remove
        + --create
        + --upload"""
        )
        sys.exit(1)
    return parser.parse_args()


def main() -> None:
    args = get_args()

    try:
        with open(args.config) as json_file:
            config_reader = deserialize.deserialize(ConfigReader, json.load(json_file))
    except IOError:
        print("Config file not accessible or readable")
        sys.exit(1)

    runner = Runner(args.root, config_reader.signature)
    if args.remotes:
        runner.add_all_remotes(config_reader.remotes, args.username, args.password)
    if args.sources:
        runner.get_all_sources()
    if args.remove:
        runner.remove_all_sources()
    if args.create:
        runner.export_all()
        runner.create_all(config_reader.configurations)
    if args.upload:
        runner.upload_all_packages(args.upload)


if __name__ == "__main__":
    main()
