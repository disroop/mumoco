"""
Test for buildersettings
"""
from src.conanbuilder.buildersettings import BuilderSettings


def test_convert_build_settings_str_empty():
    builder_settings = BuilderSettings()
    settings_str = builder_settings.convert_build_settings_str()
    assert settings_str == ""


def test_convert_build_settings_str():
    builder_settings = BuilderSettings(build_settings=["a", "b", "c"])
    settings_str = builder_settings.convert_build_settings_str()
    assert settings_str == "abc"
