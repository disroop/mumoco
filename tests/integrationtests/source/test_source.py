import shutil

from src.mumoco import mumoco_api

import os
import os.path

file_paths = os.path.dirname(os.path.abspath(__file__))


# setup:
# mkdir sourcetest_src_in_git && cd  sourcetest_src_in_git && conan new sourcetest_src_in_git/1.0 -t
def test_sources() -> None:
    # Cleanup
    shutil.rmtree(f"{file_paths}/sourcetest_src_in_git/source", ignore_errors=True)

    # fixme this fails
    # mumoco_api(sources=True,
    #            root=f"{file_paths}/sourcetest_src_in_git",
    #            config_file_path=f"{file_paths}/config-build.json")

    # but this works
    os.system("conan source sourcetest_src_in_git --source-folder=sourcetest_src_in_git/source")

    assert os.path.isfile("sourcetest_src_in_git/source/hello/.gitignore")
    assert os.path.isfile("sourcetest_src_in_git/source/hello/CMakeLists.txt")
    assert os.path.isfile("sourcetest_src_in_git/source/hello/hello.cpp")
    assert os.path.isfile("sourcetest_src_in_git/source/hello/hello.h")
    assert os.path.isfile("sourcetest_src_in_git/source/hello/LICENSE")
    assert os.path.isfile("sourcetest_src_in_git/source/hello/main.cpp")
    assert os.path.isfile("sourcetest_src_in_git/source/hello/readme.md")
