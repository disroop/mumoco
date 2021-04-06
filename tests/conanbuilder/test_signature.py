from conanbuilder.signature import Signature


def test_version():
    signature = Signature()
    assert signature.version is None


def test_version_set():
    signature = Signature()
    signature.version = "1.0.0"
    assert signature.version == "1.0.0"

