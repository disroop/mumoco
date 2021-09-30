import deserialize

import mumoco


def test_buildersettings_convert_to_string():
    config = mumoco.BuilderSettings(
        host_profile="hp",
        build_profile="bp",
        host_settings=["hs1", "hs2"],
        build_settings=["bs1", "bs2"],
        build="build",
        excludes=["ex1", "ex2", "ex3"],
        includes=["in1", "in2"],
    )
    assert (
        str(config) == "host_profile: hp\n"
        "build_profile: bp\n"
        "host_settings: ['hs1', 'hs2']\n"
        "build_settings: ['bs1', 'bs2']\n"
        "build: build\n"
        "includes: ['in1', 'in2']\n"
        "excludes: ['ex1', 'ex2', 'ex3']\n"
    )


def test_buildersettings_deserialize():
    config = mumoco.BuilderSettings(
        host_profile=".profiles/gcc-arm-none-eabi-9",
        build_profile="default",
        host_settings=["build_type=Debug", "build_type=Release"],
        build_settings=["build_type=Release"],
        build="missing",
        excludes=["cmake_vars", "gcc_arm_none_eabi"],
        includes=[],
    )

    data = {
        "host_profile": ".profiles/gcc-arm-none-eabi-9",
        "build_profile": "default",
        "host_settings": ["build_type=Debug", "build_type=Release"],
        "build_settings": ["build_type=Release"],
        "build": "missing",
        "excludes": ["cmake_vars", "gcc_arm_none_eabi"],
    }
    settings: mumoco.BuilderSettings = deserialize.deserialize(mumoco.BuilderSettings, data)
    assert config == settings
