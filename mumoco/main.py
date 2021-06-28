#!/usr/bin/python
"""
mumoco or multi module conan helps working with multiple conan package simultaneously.
"""
import argparse
import os
import sys

import cli_ui as ui

import mumoco


def add_root_argument(parser: argparse.ArgumentParser, default_path: str) -> None:
    parser.add_argument(
        "--root", type=str, required=False, default=default_path, help="Path to root folder of multi-package module"
    )


def add_config_argument(parser: argparse.ArgumentParser, default_path: str) -> None:
    parser.add_argument("--config", type=str, required=False, default=default_path, help="Path to config-build.json")


def add_root_and_config_argument(parser: argparse.ArgumentParser, default_path: str, default_json: str) -> None:
    add_root_argument(parser, default_path)
    add_config_argument(parser, default_json)


def setup_parser(main_parser: argparse.ArgumentParser) -> None:
    cwd = os.getcwd()
    default_config_json = f"{cwd}/config-build.json"
    main_parser.add_argument("--version", action="version", version=f"mumoco {mumoco.__version__}")

    actions_parser = main_parser.add_subparsers(help="available actions", dest="action")

    remote_parser = actions_parser.add_parser("remotes", help="add all remotes from config-build.json")
    add_root_and_config_argument(remote_parser, cwd, default_config_json)

    remote_parser.add_argument("--username", type=str, required=False, default="", help="User credentials")
    remote_parser.add_argument("--password", type=str, required=False, default="", help="Access token")

    source_parser = actions_parser.add_parser("sources", help="download all sources")
    add_root_and_config_argument(source_parser, cwd, default_config_json)

    remove_parser = actions_parser.add_parser("remove", help="remove all sources")
    add_root_and_config_argument(remove_parser, cwd, default_config_json)

    create_parser = actions_parser.add_parser("create", help="create all packages for all configurations")
    add_root_and_config_argument(create_parser, cwd, default_config_json)

    upload_parser = actions_parser.add_parser("upload", help="upload all generated packages")
    add_root_and_config_argument(upload_parser, cwd, default_config_json)
    upload_parser.add_argument("remote_name", type=str, help="Remote name")


def main() -> None:
    try:
        parser = argparse.ArgumentParser()
        setup_parser(parser)

        args = parser.parse_args()

        if not args.action:
            parser.print_help()
            sys.exit()

        api = mumoco.MumocoAPI(args.config, args.root)

        if args.action == "remotes":
            api.add_remotes(args.username, args.password)
        elif args.action == "sources":
            api.sources()
        elif args.action == "remove":
            api.remove()
        elif args.action == "create":
            api.create()
        elif args.action == "upload":
            api.upload(args.remote_name)
    except mumoco.Error as error:
        if error.message:
            ui.error(error.message)
        sys.exit(1)
    except KeyboardInterrupt:
        ui.warning("Interrupted by user, quitting")
        sys.exit(1)


if __name__ == "__main__":
    main()
