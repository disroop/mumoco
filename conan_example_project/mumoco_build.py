import os
import tempfile

from conans.client.conan_api import Conan

from mumoco import MumocoAPI

FILE_PATH = os.path.dirname(os.path.abspath(__file__))


def cleanup():
    conan_factory, _, _ = Conan.factory()
    conan_factory.remove(pattern="demo*", force=True)


if __name__ == "__main__":
    cleanup()
    with tempfile.TemporaryDirectory() as temp_dir:
        api = MumocoAPI(root=f"{FILE_PATH}", config_file_path=f"{FILE_PATH}/config-build.json")
        # api.sources(f"{temp_dir}/source")
        # fixme not yet working
        # open in in vscode
        api.create()
