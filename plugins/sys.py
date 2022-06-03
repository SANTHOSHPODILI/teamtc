
import re
import uuid
import socket

import psutil
import platform
from image import BOT_USERNAME
from modules.helpers.filters import filters 
from pyrogram import Client, filters
from modules.helpers.decorators import sudo_users_only, humanbytes


# FETCH SYSINFO

@Client.on_message(command(["sysinfo", f"sysinfo@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def give_sysinfo(client, message):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(client.workdir)
    psutil.disk_io_counters()
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    somsg = f"""💖 **sʏsᴛᴇᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ**
    
**PlatForm :** `{splatform}`
**PlatForm - Release :** `{platform_release}`
**PlatForm - Version :** `{platform_version}`
**Architecture :** `{architecture}`
**HostName :** `{hostname}`
**IP :** `{ip_address}`
**Mac :** `{mac_address}`
**Processor :** `{processor}`
**Ram : ** `{ram}`
**CPU :** `{cpu_len}`
**CPU FREQ :** `{cpu_freq}`
**DISK :** `{disk}`
    """
    await message.reply(somsg)
