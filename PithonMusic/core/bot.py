import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class PithonBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "PithonMusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "Bot Started"
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("ping", "بينك", "Check that bot is alive or dead"),
                        BotCommand("play", "ابدأ", "Starts playing the requested song"),
                        BotCommand("skip", "تخطي", "Moves to the next track in queue"),
                        BotCommand("pause", "ايقاف مؤقت", "Pause the current playing song"),
                        BotCommand("resume", "استمرار", "Resume the paused song"),
                        BotCommand("end", "انهاء", "Clear the queue and leave voice chat"),
                        BotCommand("shuffle", "عشوائي", "Randomly shuffles the queued playlist."),
                        BotCommand("playmode", "وضع التشغيل", "Allows you to change the default playmode for your chat"),
                        BotCommand("settings", "اعدادات", "Open the settings of the music bot for your chat.")
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Please promote Bot as Admin in Logger Group"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")