import pytest

from src.conanbuilder.remote import Remote


@pytest.fixture
def remote():
    return Remote("myName", "myUrl")


def test_default_values(remote):
    assert remote.name == "myName"
    assert remote.url == "myUrl"
    assert remote.verify_ssl is True
    assert remote.priority == 0
    assert remote.force is False
    assert remote.login is False
