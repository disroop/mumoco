import mumoco


def test_convert_config_reader_empty() -> None:
    config_reader = mumoco.ConfigReader([])
    assert config_reader.configurations == []
    assert config_reader.signature == mumoco.Signature()
    assert config_reader.remotes == []
