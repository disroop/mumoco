class Signature:
    def __init__(self):
        self.version = None
        self.channel = None
        self.user = None

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, val):
        self.__version = val

    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, val):
        self.__channel = val

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, val):
        self.__user = val