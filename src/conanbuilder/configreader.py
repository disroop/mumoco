"""
The configreader provides the functionality to read a config json file
"""
from dataclasses import dataclass, field
from typing import List

from .buildersettings import BuilderSettings
from .remote import Remote
from .signature import Signature


@dataclass
class ConfigReader:
    path: str
    configurations: List[BuilderSettings] = field(default_factory=list)
    signature: Signature = Signature()
    remotes: List[Remote] = field(default_factory=list)
