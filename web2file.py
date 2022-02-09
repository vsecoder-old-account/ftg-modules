from .. import loader, utils
import io
import requests
from telethon.tl.types import *


@loader.tds
class Web2fileMod(loader.Module):
    """Download content from link and send it as file"""
    strings = {
        'name': 'Web2file',
        'no_args': '🦊 <b>Specify link</b>',
        'fetch_error': '🦊 <b>Download error</b>',
        'loading': '🦊 <b>Downloading...</b>'
    }

    async def web2filecmd(self, message: Message) -> None:
        """Send link content as file"""
        website = utils.get_args_raw(message)
        if not website:
            await utils.answer(message, self.strings('no_args', message))
            return
        try:
            f = io.BytesIO(requests.get(website).content)
        except:
            await utils.answer(message, self.strings('fetch_error', message))
            return

        f.name = website.split('/')[-1]

        await message.respond(file=f)
        await message.delete()
