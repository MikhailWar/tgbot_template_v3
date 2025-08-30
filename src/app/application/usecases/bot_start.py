from aiogram.types import User

from app.infrastructure.database.transaction_manager import TransactionManager


class BotStartInteractor:
    def __init__(
            self,
            user: User,
    ):
        self.user = user

    async def __call__(self, *args, **kwargs) -> str:
        return f"Hello, {self.user.username}!"


class BotStartAdminInteractor:
    def __init__(
            self,
            user: User,
    ):
        self.user = user

    async def __call__(self, *args, **kwargs) -> str:
        return f"Hello, {self.user.username}! You are admin!"
