"""
The configreader provides the functionality to read a config json file
"""
import json
import sys
from typing import Dict, List

from .buildersettings import BuilderSettings
from .remote import Remote
from .signature import Signature


def __parse_configuration(conf: Dict) -> BuilderSettings:
    configuration = BuilderSettings()
    configuration.host_profile = conf.get("hostprofile", "")
    configuration.build_profile = conf.get("buildprofile", "")
    configuration.host_settings = conf.get("hostsettings", [])
    # configuration.host_build = conf.get("hostbuild")
    configuration.excludes = conf.get("excludes", [])
    configuration.includes = conf.get("includes", [])
    configuration.build = conf.get("build", "")
    return configuration


class ConfigReader:
    def __init__(self, path: str):
        self.path: str = path
        self._configurations: List[BuilderSettings] = [BuilderSettings()]
        self._signature: Signature = Signature()
        self._remotes: List[Remote] = []

    def read(self) -> None:
        try:
            with open(self.path) as json_file:
                self.__parse_data(json.load(json_file))
        except IOError:
            print("Config file not accessible or readable")
            sys.exit(1)

    def __parse_remote(self, data: Dict) -> Remote:
        if "name" not in data:
            raise ValueError(f"You need to set name if you set a remote in {self.path}")
        if "url" not in data:
            raise ValueError(f"You need to set url if you set a remote {self.path}")
        name = data.get("name", "")
        url = data.get("url", "")
        remote = Remote(name=name, url=url)
        remote.verify_ssl = data.get("verifyssl", True)
        remote.priority = data.get("priority", 0)
        remote.force = data.get("force", False)
        remote.login = data.get("login", False)
        return remote

    def __parse_data(self, data: Dict) -> None:
        self._signature.version = data.get("version", "")
        self._signature.user = data.get("user", "")
        self._signature.channel = data.get("channel", "")
        self._configurations.clear()
        for configuration_data in data.get("configurations", []):
            configuration = __parse_configuration(configuration_data)
            self._configurations.append(configuration)

        self._remotes.clear()
        for remote_data in data.get("remotes", []):
            remote = self.__parse_remote(remote_data)
            self._remotes.append(remote)

    def get_configurations(self) -> List[BuilderSettings]:
        return self._configurations

    def get_signature(self) -> Signature:
        return self._signature

    def get_remotes(self) -> List[Remote]:
        return self._remotes
