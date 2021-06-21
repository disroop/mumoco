import os
import os.path
import subprocess
import sys
import tempfile

import pytest

from src.mumoco import mumoco_api

FILE_PATH = os.path.dirname(os.path.abspath(__file__))


@pytest.mark.skip(reason="this test currently fails")
def test_sources() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        # subprocess.run(
        #     ["conan", "source", "sourcetest_src_in_git/conanfile.py", "--source-folder={}/source".format(temp_dir)],
        #     check=True,
        # )

        mumoco_api(
            sources=True,
            # source_folder="{}/source".format(temp_dir),
            root="f{file_paths}/sourcetest_src_in_git",
            config_file_path=f"{FILE_PATH}/config-build.json",
        )

        assert os.path.isfile("{}/source/hello/.gitignore".format(temp_dir))
        assert os.path.isfile("{}/source/hello/CMakeLists.txt".format(temp_dir))
        assert os.path.isfile("{}/source/hello/hello.cpp".format(temp_dir))
        assert os.path.isfile("{}/source/hello/hello.h".format(temp_dir))
        assert os.path.isfile("{}/source/hello/LICENSE".format(temp_dir))
        assert os.path.isfile("{}/source/hello/main.cpp".format(temp_dir))
        assert os.path.isfile("{}/source/hello/readme.md".format(temp_dir))
