from conanbuilder.configreader import ConfigReader
from conanbuilder.signature import Signature


def test_convert_config_reader_empty() -> None:
    config_reader = ConfigReader(list())
    assert config_reader.configurations == []
    assert config_reader.signature == Signature()
    assert config_reader.remotes == []
