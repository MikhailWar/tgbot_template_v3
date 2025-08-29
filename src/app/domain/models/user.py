from dataclasses import dataclass


@dataclass
class UserSchema:
    id: int
    first_name: str
    last_name: str
    username: str
    language_code: str


