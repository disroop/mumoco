from typing import List

from conans.client.conan_api import Conan

import mumoco


def test_runner():
    conan_factory, _, _ = Conan.factory()
    packages: List[mumoco.Package] = []
    runner = mumoco.Runner(conan_factory, packages)
    assert runner.packages == []
