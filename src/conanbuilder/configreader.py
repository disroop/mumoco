"""
The configreader provides the functionality to read a config json file
"""
from dataclasses import dataclass
from typing import List

from .buildersettings import BuilderSettings
from .remote import Remote
from .signature import Signature


@dataclass
class ConfigReader:
    path: str
    configurations: List[BuilderSettings] = [BuilderSettings()]
    signature: Signature = Signature()
    remotes: List[Remote] = []
