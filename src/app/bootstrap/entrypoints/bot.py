import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder

from src.app.bootstrap.config import load_config
from src.app.bootstrap.logging import setup_logging
from src.app.infrastructure.di.setup import get_ioc_bot_container
from src.app.presentation.bot.handlers import setup_bot_controllers
from src.app.presentation.bot.middlewares import setup_middlewares
from dishka.integrations.aiogram import setup_dishka


def get_storage(config):
    if config.tg_bot.use_redis:
        return RedisStorage.from_url(
            config.redis.dsn(),
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
        )
    else:
        return MemoryStorage()


async def main():
    setup_logging()

    config = load_config(".env")
    storage = get_storage(config)

    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode="HTML")
    )
    dp = Dispatcher(storage=storage)

    container = get_ioc_bot_container(config)
    setup_dishka(container=container, router=dp, auto_inject=True)

    setup_middlewares(dp)
    setup_bot_controllers(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Stopped bot")
