from dishka import Provider, provide_all, Scope

from app.application.usecases.bot_start import (
    BotStartAdminInteractor,
    BotStartInteractor
)


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    handlers = provide_all(
        BotStartAdminInteractor,
        BotStartInteractor,
    )

