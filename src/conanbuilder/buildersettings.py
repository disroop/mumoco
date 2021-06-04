"""
A data class representing a builder setting
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class BuilderSettings:
    host_profile: str = "default"
    build_profile: str = "default"
    host_settings: List[str] = field(default_factory=lambda: [])
    build_settings: List[str] = field(default_factory=lambda: [])
    build: str = ""
    excludes: List[str] = field(default_factory=lambda: [])
    includes: List[str] = field(default_factory=lambda: [])

    def convert_build_settings_str(self) -> str:
        return "".join(self.build_settings)
