from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram_i18n import I18nMiddleware
from dishka import AsyncContainer
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database.gateway.users import UsersGateway
from app.domain.models.user import UserSchema
from app.infrastructure.database.tables.users import User
from app.infrastructure.database.transaction_manager import TransactionManager





class UserMiddleware(BaseMiddleware):

    def __init__(self, i18n: I18nMiddleware):
        self.i18n = i18n

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:

        event_from_user: User = data["event_from_user"]

        dishka_container: AsyncContainer = data.get('dishka_container')
        transaction_manager: TransactionManager = await dishka_container.get(TransactionManager)
        session: AsyncSession = await dishka_container.get(AsyncSession)
        user_gateway = UsersGateway(session)

        language_code = self.i18n.core.default_locale
        if language_code in self.i18n.core.available_locales:
            language_code = event_from_user.language_code

        data['user'] = await user_gateway.get_user_or_create(
            user=UserSchema(
                id=event_from_user.id,
                first_name=event_from_user.first_name,
                last_name=event_from_user.last_name,
                username=event_from_user.username,
                language_code=language_code,
            )
        )
        data['transaction_manager'] = transaction_manager

        await transaction_manager.commit()

        result = await handler(event, data)

        return result
