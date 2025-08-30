import typing

from dishka import Provider

from app.infrastructure.di.providers.usecases import UseCasesProvider
from src.app.infrastructure.di.providers.application import (
    ConfigProvider, DbProvider, ApplicationProvider
)


def get_providers() -> typing.List[Provider]:

    return [
        ConfigProvider(),
        DbProvider(),
        ApplicationProvider(),
        UseCasesProvider()

    ]