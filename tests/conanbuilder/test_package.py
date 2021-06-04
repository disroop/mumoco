from unittest.mock import MagicMock, Mock

from conans.client.conan_api import Conan
from conans.errors import ConanException

from src.conanbuilder.package import Package
from src.conanbuilder.signature import Signature


def inspect_conanfile_all(*args, **kwargs):
    vals = {
        "name": {"name": "example"},
        "version": {"version": "0.0.1"},
        "user": {"user": "test"},
        "channel": {"channel": "release"},
    }
    attributes_list = kwargs["attributes"]
    attribute = attributes_list[0]
    return vals[attribute]


def inspect_conanfile_only_name(*args, **kwargs):
    vals = {"name": {"name": "example"}}
    attributes_list = kwargs["attributes"]
    attribute = attributes_list[0]
    if attribute in vals:
        return vals[attribute]
    else:
        raise ConanException


def test_get_path():
    conanfactory = Mock()
    signature = Signature()
    package = Package(conanfactory, signature, "dir")
    assert package.get_path() == "dir/"


def test_get_pattern_in_file():
    conanfactory, _, _ = Conan.factory()
    signature = Signature()
    signature.version = "1.0.0"
    signature.channel = "dev"
    signature.user = "disroop"
    conanfactory.inspect = MagicMock(side_effect=inspect_conanfile_all)
    package = Package(conanfactory, signature, "dir")
    assert package.get_pattern() == "example/0.0.1@test/release"


def test_get_pattern_by_signature():
    conanfactory, _, _ = Conan.factory()
    signature = Signature()
    signature.version = "1.0.0"
    signature.channel = "dev"
    signature.user = "disroop"
    conanfactory.inspect = MagicMock(side_effect=inspect_conanfile_only_name)
    package = Package(conanfactory, signature, "dir")
    assert package.get_pattern() == "example/1.0.0@disroop/dev"
