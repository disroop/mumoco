import deserialize
import pytest

import mumoco


@pytest.fixture
def remote():
    return mumoco.Remote("myName", "myUrl")


def test_default_values(remote):
    assert remote.name == "myName"
    assert remote.url == "myUrl"
    assert remote.verify_ssl is True
    assert remote.priority == 0
    assert remote.force is False
    assert remote.login is False


def test_remote_deserialize(remote):
    data = {
        "name": "myName",
        "url": "myUrl",
    }
    temp: mumoco.Remote = deserialize.deserialize(mumoco.Remote, data)
    assert temp == remote
