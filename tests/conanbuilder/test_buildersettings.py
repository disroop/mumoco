from src.conanbuilder.buildersettings import BuilderSettings


def test_convert_build_settings_str_empty():
    builder_settings = BuilderSettings()
    settings_str = builder_settings.convert_build_settings_str()
    assert settings_str == ""


def test_convert_build_settings_str():
    builder_settings = BuilderSettings(build_settings=["a", "b", "c"])
    settings_str = builder_settings.convert_build_settings_str()
    assert settings_str == "abc"


def test_buildersettings_convert_to_string():
    config = BuilderSettings(
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
