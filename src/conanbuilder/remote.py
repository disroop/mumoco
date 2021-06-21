"""
A data class representing a conan remote
"""
from dataclasses import dataclass

import deserialize


@dataclass
@deserialize.default("verify_ssl", True)
@deserialize.default("priority", 0)
@deserialize.default("force", False)
@deserialize.default("login", False)
class Remote:
    name: str
    url: str
    verify_ssl: bool = True
    priority: int = 0
    force: bool = False
    login: bool = False
