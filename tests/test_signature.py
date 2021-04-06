from unittest import TestCase
from conanbuilder.signature import Signature


class TestSignature(TestCase):
    def test_version_default(self):
        signature = Signature()
        self.assertEqual(None, signature.version)

    def test_version_set(self):
        signature = Signature()
        signature.version = "1.0.0"
        self.assertEqual("1.0.0", signature.version)
