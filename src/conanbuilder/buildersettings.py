from dataclasses import dataclass
from typing import List


@dataclass
class BuilderSettings:
    host_profile: str = "default"
    build_profile: str = "default"
    host_settings: List[str] = []
    build_settings: List[str] = []
    build: str = ""
    excludes: List[str] = []
    includes: List[str] = []

    def convert_build_settings_str(self) -> str:
        str_build_settings = ""
        # traverse in the string
        for settings in self.build_settings:
            str_build_settings += settings
        return str_build_settings
