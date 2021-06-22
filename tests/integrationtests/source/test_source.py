import os
import os.path
import subprocess
import sys
import tempfile

import pytest

from src.mumoco import mumoco_api

FILE_PATH = os.path.dirname(os.path.abspath(__file__))


def test_sources() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        mumoco_api(
            sources=True,
            source_folder=f"{temp_dir}/source",
            root=f"{FILE_PATH}/sourcetest_src_in_git",
            config_file_path=f"{FILE_PATH}/config-build.json",
        )

        output_dir = f"{temp_dir}/source/sourcetest_src_in_git/hello"

        assert os.path.isfile(f"{output_dir}/.gitignore")
        assert os.path.isfile(f"{output_dir}/CMakeLists.txt")
        assert os.path.isfile(f"{output_dir}/hello.cpp")
        assert os.path.isfile(f"{output_dir}/hello.h")
        assert os.path.isfile(f"{output_dir}/LICENSE")
        assert os.path.isfile(f"{output_dir}/main.cpp")
        assert os.path.isfile(f"{output_dir}/readme.md")
