"""
A data class representing a conan signature
"""
from dataclasses import dataclass

import deserialize


@dataclass
@deserialize.default("version", "")
@deserialize.default("channel", "")
@deserialize.default("user", "")
class Signature:
    version: str = ""
    channel: str = ""
    user: str = ""
