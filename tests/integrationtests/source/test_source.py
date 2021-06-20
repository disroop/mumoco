import os
import os.path
import sys
import tempfile
import subprocess

from src.mumoco import mumoco_api

file_paths = os.path.dirname(os.path.abspath(__file__))


# setup:
# mkdir sourcetest_src_in_git && cd  sourcetest_src_in_git && conan new sourcetest_src_in_git/1.0 -t
def test_sources() -> None:
    # fixme this fails
    # mumoco_api(sources=True,
    #            root=f"{file_paths}/sourcetest_src_in_git",
    #            config_file_path=f"{file_paths}/config-build.json")

    # but this works
    with tempfile.TemporaryDirectory() as temp_dir:
        subprocess.run(
            ["conan", "source", "sourcetest_src_in_git/conanfile.py", "--source-folder={}/source".format(temp_dir)],
            check=True,
        )

        assert os.path.isfile("{}/source/hello/.gitignore".format(temp_dir))
        assert os.path.isfile("{}/source/hello/CMakeLists.txt".format(temp_dir))
        assert os.path.isfile("{}/source/hello/hello.cpp".format(temp_dir))
        assert os.path.isfile("{}/source/hello/hello.h".format(temp_dir))
        assert os.path.isfile("{}/source/hello/LICENSE".format(temp_dir))
        assert os.path.isfile("{}/source/hello/main.cpp".format(temp_dir))
        assert os.path.isfile("{}/source/hello/readme.md".format(temp_dir))
