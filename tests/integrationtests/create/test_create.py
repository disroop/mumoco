from argparse import Namespace

import pytest

# Test 1
# when
# create_test_package(a) ( with conan new mycreatetestA/1.0)
# create_test_package(b) ( with conan new mycreatetestB/1.0)
# create_test_package(c) ( with conan new mycreatetestC/1.0)
# addDependency(a, [b])
# addDependency(b, [c])
# C must be build first, then B, Then A

# then
# momoco --create
# builds C first
# then build B
# then builds A

# Test this eather by adding a log in the build() or find a even better
# solution wtih plan python and multiple conan and simple state variables

# ... what eslse?


@pytest.mark.skip(reason="this test currently fails")
def test_create():
    assert True
