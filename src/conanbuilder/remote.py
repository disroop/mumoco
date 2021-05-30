from dataclasses import dataclass


@dataclass
class Remote:
    name: str
    url: str
    verify_ssl: bool = True
    priority: int = 0
    force: bool = False
    login: bool = False
