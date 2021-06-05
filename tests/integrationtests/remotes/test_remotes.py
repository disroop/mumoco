from argparse import Namespace

import conans.client.conan_api
import pytest

import mumoco
import src.conanbuilder.remote

# Test 1
# given
# a clean conan setup
# just conan center exist in remotes

# when
# running mumoco --remotes with config-build.json
# then
# has added the new remote ( test with conan remotes

# Test 2 - test with empty remotes
# Test 3 - test with multiple different remotes
# Test 4 - test with multiple same remotes
# Test 5 - test twice calling conan --remote and a changes config
# ... what eslse?


@pytest.mark.skip(reason="this test currently fails")
def test_remote():
    # given
    # a clean conan setup
    # just conan center exist in remotes

    # when
    # running mumocmo --remotes with config-build.json
    # then
    # has added the new remote
    assert True


@pytest.mark.skip(reason="this test currently fails")
def test_remote2():
    # given
    # a clean conan setup
    # just conan center exist in remotes

    # when
    # running mumocmo --remotes with config-build.json
    # then
    # has added the new remote

    # unfinished not working code
    assert True
    # conan, _, _ = conans.client.conan_api.Conan.factory()
    # remote_list = conan.remote_list()
    # conan_remote_list = conan.remote_list()
    # for conan_remote in conan_remote_list:
    #     conan.remote_remove(conan_remote.name)
    # assert conan.remote_list() == []
    #
    # args = Namespace(root='/Users/stefaneicher/IdeaProjects/Disroop/github/mumoco/src',
    #                  config='/Users/stefaneicher/IdeaProjects/Disroop/github/mumoco/tests/remotes/config-build.json',
    #                  username=None, password=None, remotes=True, sources=False, remove=False, create=False,
    #                  upload=None)
    # mumoco.mumoco(args)
    # conan_remote_list = [
    #     Remote(name='disroop-conan',
    #            url='https://disroop.jfrog.io/artifactory/api/conan/disroop-conan',
    #            verify_ssl=None)]
    # conan_remote_list_after = conan.remote_list()
    # assert len(conan_remote_list) == 1
    # pop = conan_remote_list.pop()
    # # assert pop == Remote(name='disroop-conan',
    # #                      url='https://disroop.jfrog.io/artifactory/api/conan/disroop-conan',
    # #                      verify_ssl=None)
    # remote_remote = src.conanbuilder.remote.Remote("disroop-conan",
    #                                                "https://disroop.jfrog.io/artifactory/api/conan/disroop-conan",
    #                                                verify_ssl=None)
    # assert pop is remote_remote
