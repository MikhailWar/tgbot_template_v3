from dataclasses import dataclass


@dataclass
class UserSchema:
    id: int
    first_name: str
    last_name: str | None
    username: str | None
    language_code: str


