from .. import loader, utils 
from asyncio import sleep 
 
@loader.tds 
class TextFormatMod(loader.Module): 
    """Автозамена""" 
    strings = {'name': 'Formater'} 
    @loader.owner
    async def formatcmd(self, message):
        message.edit('test')
