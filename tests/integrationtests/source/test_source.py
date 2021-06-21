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
            source_folder="{}/source".format(temp_dir),
            root=f"{FILE_PATH}/sourcetest_src_in_git",
            config_file_path=f"{FILE_PATH}/config-build.json",
        )

        output_dir = "{}/source/sourcetest_src_in_git/hello".format(temp_dir)

        assert os.path.isfile("{}/.gitignore".format(output_dir))
        assert os.path.isfile("{}/CMakeLists.txt".format(output_dir))
        assert os.path.isfile("{}/hello.cpp".format(output_dir))
        assert os.path.isfile("{}/hello.h".format(output_dir))
        assert os.path.isfile("{}/LICENSE".format(output_dir))
        assert os.path.isfile("{}/main.cpp".format(output_dir))
        assert os.path.isfile("{}/readme.md".format(output_dir))
