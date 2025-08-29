import typing

from dishka import Provider

from src.app.infrastructure.di.providers.application import (
    ConfigProvider, DbProvider, ApplicationProvider
)


def get_providers() -> typing.List[Provider]:

    return [
        ConfigProvider(),
        DbProvider(),
        ApplicationProvider()
    ]