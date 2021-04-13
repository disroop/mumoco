#!/usr/bin/python
import argparse
import os

from src.conanbuilder.configreader import ConfigReader
from src.conanbuilder.runner import Runner


def get_args():
    cwd = os.getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=str, required=False, default=cwd,
                        help="Path to root folder of multipackage module")
    parser.add_argument("--config", type=str, required=False, default=f"{cwd}/config-build.json",
                        help="Path to config-build.json")
    parser.add_argument("--sources", action="store_true", required=False, help="Download sources to PACKAGE-PATH/tmp")
    parser.add_argument("--remove", action="store_true", required=False, help="Remove all sources")
    parser.add_argument("--create", action="store_true", required=False, help="Create all packages")
    parser.add_argument("--upload", type=str, required=False, help="Upload all packages to repository")
    parser.add_argument("--remotes", action="store_true", required=False, help="Add all remotes from config-build.json")
    parser.add_argument("--user", type=str, required=False, default=None, help="User credentials")
    parser.add_argument("--password", type=str, required=False, default=None, help="Access token")
    return parser.parse_args()

def main():
    args = get_args();
    config_reader = ConfigReader(args.config)
    config_reader.read()
    runner = Runner(args.root, config_reader.get_signature())
    if args.remotes:
        runner.add_all_remotes(config_reader.get_remotes(), args.user, args.password)
    if args.create:
        runner.export_all()
        runner.create_all(config_reader.get_configurations())
    if args.sources:
        runner.get_all_sources()
    if args.remove:
        runner.remove_all_sources()
    if args.upload:
        runner.upload_all_packages(args.upload)

if __name__ == "__main__":
    main()
    # create_all(packages,config_reader.get_configurations())
    # packages[0].get_build_order(config_reader.get_configurations()[0])
