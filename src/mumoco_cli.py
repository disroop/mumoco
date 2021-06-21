#!/usr/bin/python
"""
mumoco or multi module conan helps working with multiple conan package simultaneously.
"""
import argparse
import os
import sys

from src import mumoco
from src.exceptions import MumocoInvalidCommand


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
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    try:
        mumoco.mumoco_api(
            args.upload,
            args.remove,
            args.create,
            args.remotes,
            args.sources,
            args.username,
            args.password,
            args.root,
            args.config,
        )
    except MumocoInvalidCommand as err:
        print(err)
        sys.exit(1)
