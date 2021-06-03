from dataclasses import dataclass


@dataclass
class Signature:
    version: str = ""
    channel: str = ""
    user: str = ""
