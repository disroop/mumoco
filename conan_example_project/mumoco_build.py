import os
import tempfile

from mumoco_api import MumocoAPI

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as temp_dir:
        # run this before
        # os.run("conan export Base  disroopbase/0.1@disroop/development")
        api = MumocoAPI(root=f"{FILE_PATH}", config_file_path=f"{FILE_PATH}/config-build.json")
        # api.sources(f"{temp_dir}/source")
        #fixme not yet working
        # open in in vscode
        api.create()
