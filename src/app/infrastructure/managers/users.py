from aiogram_i18n.managers import BaseManager

from app.infrastructure.database.tables.users import User
from app.infrastructure.database.transaction_manager import TransactionManager


class UserManager(BaseManager):

    async def set_locale(
            self,
            locale: str,
            user: User,
            transaction_manager: TransactionManager,
    ):
        user.language_code = locale
        await transaction_manager.commit()

    async def get_locale(self, user: User) -> str:
        return user.language_code
