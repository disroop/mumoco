import os
import tempfile

from src.mumoco_api import MumocoAPI

FILE_PATH = os.path.dirname(os.path.abspath(__file__))


def test_sources() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        api = MumocoAPI(root=f"{FILE_PATH}/sourcetest_src_in_git", config_file_path=f"{FILE_PATH}/config-build.json")
        api.sources(f"{temp_dir}/source")

        output_dir = f"{temp_dir}/source/sourcetest_src_in_git/hello"

        assert os.path.isfile(f"{output_dir}/.gitignore")
        assert os.path.isfile(f"{output_dir}/CMakeLists.txt")
        assert os.path.isfile(f"{output_dir}/hello.cpp")
        assert os.path.isfile(f"{output_dir}/hello.h")
        assert os.path.isfile(f"{output_dir}/LICENSE")
        assert os.path.isfile(f"{output_dir}/main.cpp")
        assert os.path.isfile(f"{output_dir}/readme.md")
