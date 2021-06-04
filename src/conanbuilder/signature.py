"""
A data class representing a conan signature
"""
from dataclasses import dataclass


@dataclass
class Signature:
    version: str = ""
    channel: str = ""
    user: str = ""
