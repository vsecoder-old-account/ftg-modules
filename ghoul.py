import io
import inspect
from .. import loader, utils
from asyncio import sleep
from math import floor

from telethon.tl.types import *

@loader.tds
class GULMod(loader.Module):
    """Show other chat members that you are ghoul"""
    strings = {
        'name': 'Ghoul',
        'iamghoul': "<b>I am ghoul!</b>"
    }

    async def гульcmd(self, message: Message) -> None:
        """Sends ghoul message"""
        x = 1000
        emojies = ['⚫️', '⚪️', '⬜️']
        await message.edit(self.strings('iamghoul', message))
        await sleep(2)
        while x > 0:
            await message.edit(emojies[floor((1000 - x) / (1000 / len(emojies)))] + str(x) + " - 7 = " + str(x-7))
            x -= 7
            await sleep(1)
