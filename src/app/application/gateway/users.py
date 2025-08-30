from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models.user import UserSchema
from app.infrastructure.database.tables.users import User


class UsersGateway:
    def __init__(
            self,
            session: AsyncSession,
    ):
        self.session = session


    async def get_user_or_create(self, user: UserSchema) -> User:

        stmt = insert(
            User
        ).values(
            id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            language=user.language_code
        ).on_conflict_do_update(
            index_elements=[User.id],
            set_=dict(
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
            )
        ).returning(User)
        response = await self.session.execute(stmt)

        return response.scalar()



