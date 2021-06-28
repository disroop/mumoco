import os

from conans.client.conan_api import Conan

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    conan_factory, _, _ = Conan.factory()
    conan_factory.create(f"{FILE_PATH}/a", version="0.1", user="disroop", channel="development")
    conan_factory.create(f"{FILE_PATH}/b", version="0.1", user="disroop", channel="development")
    conan_factory.create(f"{FILE_PATH}/c", version="0.1", user="disroop", channel="development")
    conan_factory.create(f"{FILE_PATH}/d", version="0.1", user="disroop", channel="development")
