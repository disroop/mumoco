class Remote:
    def __init__(self, name, url, verify_ssl=True, priority=0, force=False, login=False):
        self._name: str = name
        self._url: str = url
        self._verify_ssl: bool = verify_ssl
        self._priority: int = priority
        self._force: bool = force
        self._login: bool = login

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @property
    def verify_ssl(self):
        return self._verify_ssl

    @verify_ssl.setter
    def verify_ssl(self, val):
        self._verify_ssl = val

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, val):
        self._priority = val

    @property
    def force(self):
        return self._force

    @force.setter
    def force(self, val):
        self._force = val

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, val):
        self._login = val
