from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message
from dishka import AsyncContainer
from sqlalchemy.ext.asyncio import AsyncSession
from app.application.gateway.users import UsersGateway
from app.domain.models.user import UserSchema
from app.infrastructure.database.transaction_manager import TransactionManager


class UserMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:


        dishka_container: AsyncContainer = data.get('dishka_container')
        transaction_manager: TransactionManager = await dishka_container.get(TransactionManager)
        session: AsyncSession = await dishka_container.get(AsyncSession)
        user_gateway = UsersGateway(session)
        data['user'] = await user_gateway.get_user_or_create(
            user=UserSchema(
                id=event.from_user.id,
                first_name=event.from_user.first_name,
                last_name=event.from_user.last_name,
                username=event.from_user.username,
                language_code=event.from_user.language_code,
            )
        )
        await transaction_manager.commit()

        result = await handler(event, data)

        return result
