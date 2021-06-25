import deserialize
import pytest

import mumoco


@pytest.fixture
def signature():
    return mumoco.Signature()


def test_version(signature):
    assert not signature.version


def test_version_set(signature):
    signature.version = "1.0.0"
    assert signature.version == "1.0.0"


def test_channel(signature):
    assert not signature.channel


def test_channel_set(signature):
    signature.channel = "dev"
    assert signature.channel == "dev"


def test_user(signature):
    assert not signature.user


def test_user_set(signature):
    signature.user = "user"
    assert signature.user == "user"


def test_signature_deserialize():
    signature = mumoco.Signature(version="1.2.3", channel="user", user="ypsomed")
    data = {"version": "1.2.3", "channel": "user", "user": "ypsomed"}
    temp: mumoco.Signature = deserialize.deserialize(mumoco.Signature, data)
    assert temp == signature
