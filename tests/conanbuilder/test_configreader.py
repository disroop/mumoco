from conanbuilder.configreader import ConfigReader
from conanbuilder.signature import Signature


def test_convert_config_reader_empty() -> None:
    config_reader = ConfigReader("myPath", list())
    assert config_reader.path == "myPath"
    assert config_reader.configurations == []
    assert config_reader.signature == Signature()
    assert config_reader.remotes == []
