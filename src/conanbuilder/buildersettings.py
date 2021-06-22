"""
A data class representing a builder setting
"""
from dataclasses import dataclass, field
from typing import List

import deserialize


@dataclass
@deserialize.default("host_profile", "default")
@deserialize.default("build_profile", "default")
@deserialize.default("host_settings", [])
@deserialize.default("build_settings", [])
@deserialize.default("excludes", [])
@deserialize.default("includes", [])
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

    def __str__(self) -> str:
        return (
            f"host_profile: {self.host_profile}\n"
            + f"build_profile: {self.build_profile}\n"
            + f"host_settings: {self.host_settings}\n"
            + f"build_settings: {self.build_settings}\n"
            + f"build: {self.build}\n"
            + f"includes: {self.includes}\n"
            + f"excludes: {self.excludes}\n"
        )
