import os
import tempfile

from conans.client.conan_api import Conan

from mumoco import MumocoAPI

FILE_PATH = os.path.dirname(os.path.abspath(__file__))


def cleanup() -> None:
    conan_factory, _, _ = Conan.factory()
    conan_factory.remove(pattern="demo*", force=True)
    # workaround mumoco: cant deal with conan base packages
    conan_factory.export(f"{FILE_PATH}/Base", "disroopbase", "0.1", "disroop", "development")


if __name__ == "__main__":

    cleanup()
    with tempfile.TemporaryDirectory() as temp_dir:
        api = MumocoAPI(root=f"{FILE_PATH}", config_file_path=f"{FILE_PATH}/mumoco.json")
        api.create()
