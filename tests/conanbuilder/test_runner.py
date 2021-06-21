from typing import List

from conans.client.conan_api import Conan

from src.conanbuilder.package import Package
from src.conanbuilder.runner import Runner


def test_runner():
    conan_factory, _, _ = Conan.factory()
    packages: List[Package] = []
    runner = Runner(conan_factory, packages)
    assert runner.packages == []
