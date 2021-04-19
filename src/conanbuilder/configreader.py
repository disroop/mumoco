import json

from .signature import Signature
from .buildersettings import BuilderSettings
from .remote import Remote


class ConfigReader:
    def __init__(self, path):
        self.path = path
        self._configurations = [BuilderSettings()]
        self._signature = Signature()
        self._remotes = []

    def read(self):
        try:
            with open(self.path) as json_file:
                data = json.load(json_file)
                if 'version' in data:
                    self._signature.version = data['version']
                if 'user' in data:
                    self._signature.user = data['user']
                if 'channel' in data:
                    self._signature.channel = data['channel']
                if 'configurations' in data:
                    self._configurations = []
                    for p in data['configurations']:
                        configuration = BuilderSettings()
                        if 'hostprofile' in p:
                            configuration.host_profile = p['hostprofile']
                        if 'buildprofile' in p:
                            configuration.build_profile = p['buildprofile']
                        if 'hostsettings' in p:
                            configuration.host_settings = p['hostsettings']
                        if 'hostbuild' in p:
                            configuration.host_build = p['hostbuild']
                        if 'excludes' in p:
                            configuration.excludes = p['excludes']
                        if 'includes' in p:
                            configuration.includes = p['includes']
                        if 'build' in p:
                            configuration.build = p['build']
                        self._configurations.append(configuration)
                if 'remotes' in data:
                    self._remotes = []
                    for p in data['remotes']:
                        if 'name' not in p:
                            raise ValueError(
                                f"You need to set name if you set a remote in {self.path}")
                        if 'url' not in p:
                            raise ValueError(
                                f"You need to set url if you set a remote {self.path}")
                        name = p['name']
                        url = p['url']
                        remote = Remote(name=name, url=url)
                        if 'verifyssl' in p:
                            remote.verify_ssl = p['verifyssl']
                        if 'priority' in p:
                            remote.priority = p['priority']
                        if 'force' in p:
                            remote.force = p['force']
                        if 'login' in p:
                            remote.login = p['login']
                        self._remotes.append(remote)
        except IOError:
            print("Config file not accessible or readable")
            exit(1)

    def get_configurations(self):
        return self._configurations

    def get_signature(self):
        return self._signature

    def get_remotes(self):
        return self._remotes
