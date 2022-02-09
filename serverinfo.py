from .. import loader, utils
import os
import psutil
import platform
import sys
from telethon.tl.types import *

# requires: psutil


def b2mb(b):
    return round(b / 1024 / 1024, 1)


def find_lib(lib):
    try:
        if lib == 'Telethon':
            lib = 'Telethon | grep -v Telethon-Mod'
        ver = os.popen('python3 -m pip freeze | grep ' +
                       lib).read().split('==')[1]
        if '\n' in ver:
            return ver.split('\n')[0]
        return ver
    except:
        return 'Not Installed'


@loader.tds
class serverInfoMod(loader.Module):
    """Show server info"""
    strings = {
        "name": "ServerInfo",
        "loading": "<b>👾 Loading server info...</b>",
        "servinfo": "<b><u>👾 Server Info:</u>\n\n<u>🗄 Used resources:</u>\n    CPU: {} Cores {}%\n    RAM: {} / {}MB ({}%)\n\n<u>🧾 Dist info</u>\n    Kernel: {}\n    Arch: {}\n    OS: {}\n\n<u>📦 Python libs:</u>\n    Telethon: {}\n    Telethon-Mod: {}\n    Python-Git: {}\n    Python: {}\n    Pip: {}</b>"
    }

    async def serverinfocmd(self, message):
        """Show server info"""
        message = await utils.answer(message, self.strings('loading'))
        try:
            message = message[0]
        except:
            pass

        inf = []
        try:
            inf.append(psutil.cpu_count(logical=True))
        except:
            inf.append('n/a')

        try:
            inf.append(psutil.cpu_percent())
        except:
            inf.append('n/a')

        try:
            inf.append(b2mb(psutil.virtual_memory().total -
                            psutil.virtual_memory().available))
        except:
            inf.append('n/a')

        try:
            inf.append(b2mb(psutil.virtual_memory().total))
        except:
            inf.append('n/a')

        try:
            inf.append(psutil.virtual_memory().percent)
        except:
            inf.append('n/a')

        try:
            inf.append(utils.escape_html(platform.release()))
        except:
            inf.append('n/a')

        try:
            inf.append(utils.escape_html(platform.architecture()[0]))
        except:
            inf.append('n/a')

        try:
            system = os.popen('cat /etc/*release').read()
            b = system.find('DISTRIB_DESCRIPTION="') + 21
            system = system[b:system.find('"', b)]
            inf.append(utils.escape_html(system))
        except:
            inf.append('n/a')

        try:
            inf.append(find_lib('Telethon'))
        except:
            inf.append('n/a')

        try:
            inf.append(find_lib('Telethon-Mod'))
        except:
            inf.append('n/a')

        try:
            inf.append(find_lib('python-git'))
        except:
            inf.append('n/a')

        try:
            inf.append(f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        except:
            inf.append('n/a')

        try:
            inf.append(os.popen('python3 -m pip --version').read().split()[1])
        except:
            inf.append('n/a')

        await utils.answer(message, self.strings('servinfo').format(*inf))
