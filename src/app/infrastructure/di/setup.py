from dishka import AsyncContainer, make_async_container
from dishka.integrations.aiogram import AiogramProvider

from app.bootstrap.config import Config
from app.infrastructure.di import providers


def get_ioc_bot_container(config: Config) -> AsyncContainer:

    return make_async_container(
        AiogramProvider(),
        *providers.get_providers(),
        context={
            Config: config,
        }
    )
