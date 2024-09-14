import motor.motor_asyncio
import asyncio
import logging
import inspect
from pyrogram import Client, enums
from aiohttp import ClientSession
from typing import Union
from .config import Config
from .translation import Translation


class BotClient(Client):

    def __init__(self):  # Corrected to __init__ method
        super().__init__(  # Initialize the base class
            name='X-URL-Uploader',
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins={'root': 'Bot.plugins'},
            parse_mode=enums.ParseMode.HTML
        )
        self.sleep = asyncio.sleep
        self.session: ClientSession = None
        self.config = Config
        self.translation = Translation
        self.database: Union[motor.motor_asyncio.AsyncIOMotorClient, None] = motor.motor_asyncio.AsyncIOMotorClient(
            self.config.DATABASE_URL) if self.config.DATABASE_URL else None
        self.custom_thumbnail = {}
        self.custom_caption = {}

    async def startup(self):
        await self.start()  # Corrected to use the instance method of the base class

    @property
    def logger(self) -> logging.Logger:
        module = inspect.getmodule(inspect.stack()[1][0])
        module_name = module.__name__ if module else 'main'  # Use __name__ for module name
        return logging.getLogger(module_name)


client = BotClient()
