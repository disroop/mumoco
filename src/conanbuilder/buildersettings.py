class BuilderSettings:
    def __init__(self):
        self.__host_profile = "default"
        self.__build_profile = "default"
        self.__host_settings = ""
        self.__build="missing"
        self.__excludes = []
        self.__includes = []

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

    @property
    def includes(self):
        return self.__includes

    @includes.setter
    def includes(self, val):
        self.__includes = val

    @property
    def build(self):
        return self.__build

    @build.setter
    def build_modes(self, val):
        self.__build = val
