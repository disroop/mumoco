class BuilderSettings:
    def __init__(self):
        self.host_profile = None
        self.build_profile = None
        self.host_settings = ""
        self.excludes = []
        self.includes = []

    @property
    def host_profile(self):
        return self.__host_profile

    @host_profile.setter
    def host_profile(self, val):
        self.__host_profile = val

    @property
    def build_profile(self):
        return self.__build_profile

    @build_profile.setter
    def build_profile(self, val):
        self.__build_profile = val

    @property
    def host_settings(self):
        return self.__host_settings

    @host_settings.setter
    def host_settings(self, val):
        self.__host_settings = val

    @property
    def excludes(self):
        return self.__excludes

    @excludes.setter
    def excludes(self, val):
        self.__excludes = val
