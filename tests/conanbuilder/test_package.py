from unittest.mock import Mock

from src.conanbuilder.package import Package
from src.conanbuilder.signature import Signature


def test_get_path():
    conanfactory = Mock()
    signature = Signature()
    package = Package(conanfactory, signature, "dir")
    assert package.path == "dir/"
