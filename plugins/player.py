## ┬ęcopyright infringement on Team Shadow Projects
## support: https://t.me/tgshadow_fighters
## network: https://t.me/teamshadowprojects



import os
import aiofiles
import aiohttp
import ffmpeg
import requests
from os import path
from asyncio.queues import QueueEmpty
from typing import Callable
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserAlreadyParticipant
from modules.cache.admins import set
from modules.clientbot import clientbot, queues
from modules.clientbot.clientbot import client as USER
from modules.helpers.admins import get_administrators
from youtube_search import YoutubeSearch
from modules import converter
from modules.downloaders import youtube
from modules.config import DURATION_LIMIT, que, SUDO_USERS
from modules.cache.admins import admins as a
from modules.helpers.filters import command, other_filters
from modules.helpers.command import commandpro
from modules.helpers.decorators import errors, authorized_users_only
from modules.helpers.errors import DurationLimitError
from modules.helpers.gets import get_url, get_file_name
from PIL import Image, ImageFont, ImageDraw
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from image import BOT_USERNAME, GROUP_SUPPORT

# plus
chat_id = None
useer = "NaN"


def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(filename)


# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    return image.resize((newWidth, newHeight))


async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open("resource/TeamShadow.jpg")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("resource/font.otf", 32)
    draw.text((190, 550), f"Title: {title[:50]} ...", (255, 255, 255), font=font)
    draw.text((190, 590), f"Duration: {duration}", (255, 255, 255), font=font)
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text(
        (190, 670),
        f"Powered By: Team Shadow (@tgshadow_fighters)",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")


@Client.on_message(
    commandpro(["/play", "/yt", "/ytp", "play", "yt", "ytp", "@", "#"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer
    
    lel = await message.reply("**­čśĺ s╔ś╔Ĺ╔ĄĂł╔Ž╔ę╔│╩Ť ╩Ćß┤Ćß┤ť╩Ç sß┤Ć╔┤╔ó ╩Çß┤Ç ╔┤╔¬╩Ö╩Öß┤Ç...**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "tgshadow_fighters"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "**ß┤Ç╩Çß┤ç╩Ć ╔┤ß┤Ç ╩Öß┤Çß┤Ťß┤Ťß┤Ç ß┤Źß┤ť╔┤ß┤ůß┤Ç╩čß┤Ç ╔┤ß┤Ç╔┤ß┤ť ß┤Çß┤ůß┤Ź╔¬╔┤ ß┤ä╩ťß┤çs╔¬ ß┤ä╩ťß┤Çß┤áß┤ť ╩Çß┤Ç­čśí.**")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "** ­čśÄ ß┤çß┤śß┤ťß┤ůß┤ť ß┤äß┤Ć╩Ç╩Çß┤çß┤äß┤Ť ╔óß┤Ç ß┤ť╔┤ß┤Çß┤á ╔┤ß┤ç╔┤ß┤ť ß┤Źß┤Ç╩Ç╔¬ ß┤ś╩čß┤Ç╩Ć ß┤ä╩ťß┤ç╩Ćß┤Ç ß┤Ťß┤Ç╔┤╔¬ß┤ő╔¬ ╩Çß┤çß┤Çß┤ů╩Ć...**")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"**­čÄŞ ß┤Çss╔¬sß┤Ťß┤Ç╔┤ß┤Ť ╔┤╔¬ ß┤Ç╩Ć╔¬╔┤ß┤Ç ß┤Çß┤ůß┤ů ß┤ä╩ťß┤ç╩Ć╔¬ ╩čß┤çß┤ů╩ťß┤Ç ß┤Źß┤Ç ╔ó╩Çß┤Ćß┤ťß┤ś ╔┤╔¬ ß┤äß┤Ć╔┤ß┤Ťß┤Çß┤äß┤Ť ß┤Çß┤ťß┤á ß┤śß┤Ćß┤íß┤ç╩Çß┤çß┤ů ╩Ö╩Ć: [ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í](https://t.me/tgshadow_fighters)­čąÇ** ")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"**­čÄŞ  ß┤Çss╔¬sß┤Ťß┤Ç╔┤ß┤Ť ╔┤╔¬ ß┤Ç╩Ć╔¬╔┤ß┤Ç ß┤Çß┤ůß┤ů ß┤ä╩ťß┤ç╩Ć╔¬ ╩čß┤çß┤ů╩ťß┤Ç ß┤Źß┤Ç ╔ó╩Çß┤Ćß┤ťß┤ś ╔┤╔¬ ß┤äß┤Ć╔┤ß┤Ťß┤Çß┤äß┤Ť ß┤Çß┤ťß┤á ß┤śß┤Ćß┤íß┤ç╩Çß┤çß┤ů ╩Ö╩Ć: [ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í](https://t.me/tgshadow_fighters)­čąÇ...**")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"**ÔŁú´ŞĆ ß┤Źß┤ťs╔¬ß┤ä ­čÄÂ ╔┤╔¬ ß┤ś╩čß┤Ç╩Ć ß┤ä╩ťß┤çsß┤Ť╩ťß┤ç ß┤ç ß┤ůß┤ť╩Çß┤Çß┤Ť╔¬ß┤Ć╔┤ ╩čß┤Ć╔┤ß┤ç ß┤ś╩čß┤Ç╩Ć ß┤ä╩ťß┤ç╩Ć╔¬ ß┤Ćß┤ő ╔┤ß┤Ç {DURATION_LIMIT}..**"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://te.legra.ph/file/02daf1a0d434a29f9d54c.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ÔÇó ß┤Źß┤ç╔┤ß┤ť", switch_inline_query_current_chat=""),
                        InlineKeyboardButton(
                            "­čŚĹ ╩Ö╔¬╔┤", callback_data="set_close"
                        ),
                    ]
                ]
           )

        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ÔÇó ß┤Źß┤ç╔┤ß┤ť", switch_inline_query_current_chat=""),
                        InlineKeyboardButton(
                            "­čŚĹ ╩Ö╔¬╔┤", callback_data="set_close"
                        ),
                    ]
                ]
           )

        except Exception as e:
            title = "NaN"
            thumb_name = "https://te.legra.ph/file/02daf1a0d434a29f9d54c.jpg"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ÔÇó ß┤Źß┤ç╔┤ß┤ť", switch_inline_query_current_chat=""),
                        InlineKeyboardButton(
                            "­čŚĹ ╩Ö╔¬╔┤", callback_data="set_close"
                        ),
                    ]
                ]
           )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**ÔŁú´ŞĆ ß┤Źß┤ťs╔¬ß┤ä ­čÄÂ ╔┤╔¬ ß┤ś╩čß┤Ç╩Ć ß┤ä╩ťß┤çsß┤Ť╩ťß┤ç ß┤ç ß┤ůß┤ť╩Çß┤Çß┤Ť╔¬ß┤Ć╔┤ ╩čß┤Ć╔┤ß┤ç ß┤ś╩čß┤Ç╩Ć ß┤ä╩ťß┤ç╩Ć╔¬ ß┤Ćß┤ő ╔┤ß┤Ç {DURATION_LIMIT}..**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit(
                "**ß┤Źß┤ťs╔¬ß┤ä ╔┤ß┤Çß┤Źß┤ç ß┤çß┤áß┤Ç╩Çß┤Ç ╔┤ß┤Ç ╩Öß┤Çß┤Ťß┤Ťß┤Ç.....**"
            )
        await lel.edit("**­čĺô ß┤ś╩Çß┤Ćß┤äß┤çss╔¬╔┤╔ó ╩Ćß┤Ćß┤ť╩Ç ß┤Źß┤ťs╔¬ß┤ä ╩Çß┤Ç ╔┤╔¬╩Ö╩Öß┤Ç/╔┤╔¬╩Ö╩Ö╔¬...**")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**╔┤ß┤á ß┤Ť╩Ćß┤śß┤ç ß┤ä╩ťß┤çs╔¬╔┤ß┤Ç ß┤Źß┤ťs╔¬ß┤ä ╔┤ß┤Çß┤őß┤ť ß┤ůß┤Ć╩Çß┤őß┤Ç ╩čß┤çß┤ů╩ťß┤ť ╩Çß┤Ç ╔┤ß┤Ç ÔŁĄ ß┤ůß┤Ç ╔óß┤Ç...**"
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ÔÇó ß┤Źß┤ç╔┤ß┤ť", switch_inline_query_current_chat=""),
                        InlineKeyboardButton(
                            "­čŚĹ ╩Ö╔¬╔┤", callback_data="set_close"
                        ),
                    ]
                ]
           )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**ÔŁú´ŞĆ ß┤Źß┤ťs╔¬ß┤ä ­čÄÂ ╔┤╔¬ ß┤ś╩čß┤Ç╩Ć ß┤ä╩ťß┤çsß┤Ť╩ťß┤ç ß┤ç ß┤ůß┤ť╩Çß┤Çß┤Ť╔¬ß┤Ć╔┤ ╩čß┤Ć╔┤ß┤ç ß┤ś╩čß┤Ç╩Ć ß┤ä╩ťß┤ç╩Ć╔¬ ß┤Ćß┤ő ╔┤ß┤Ç {DURATION_LIMIT} ...**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_photo(
            photo="final.png",
            caption=f"**ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í ß┤Çß┤ůß┤ůß┤çß┤ů sß┤Ć╔┤╔ó ß┤Çß┤Ť ß┤śß┤Ćs╔¬ß┤Ť╔¬ß┤Ć╔┤ÔŁú´ŞĆ...**\n­čÜę**╩Çß┤çăźß┤ťß┤çsß┤Ť ╩Ö╩Ć: {message.from_user.mention()}**\n­čĺô **ß┤śß┤Ćß┤íß┤ç╩Çß┤çß┤ů ╩Ö╩Ć**: [ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í](https://t.me/{GROUP_SUPPORT})".format(), 
            reply_markup=keyboard,
        )
    else:
        await clientbot.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )  

        await message.reply_photo(
            photo="final.png",
            reply_markup=keyboard,
            caption=f"**ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í ß┤Źß┤ťs╔¬ß┤ä ╔┤ß┤Ćß┤í ß┤ś╩čß┤Ç╩Ć╔¬╔┤╔ó.­čśŹ ß┤ĆĂĄ ­čąÇ** ...\n­čÜę**╩Çß┤çăźß┤ťß┤çsß┤Ť ╩Ö╩Ć: {message.from_user.mention()}**\n­čĺô **ß┤śß┤Ćß┤íß┤ç╩Çß┤çß┤ů ╩Ö╩Ć**: [ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í](https://t.me/{GROUP_SUPPORT})".format(),
           )

    os.remove("final.png")
    return await lel.delete()
    
    
@Client.on_message(commandpro(["/pause", "pause"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await clientbot.pytgcalls.pause_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://te.legra.ph/file/f97d33cc9b0f7beccf0d9.jpg", 
                             caption="**ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í ╔┤ß┤Ćß┤í ß┤śß┤Çß┤ťsß┤çß┤ů ß┤äß┤ť╩Ç╩Çß┤ç╔┤ß┤Ť╩č╩Ć ß┤ś╩čß┤Ç╩Ć╔¬╔┤╔ó sß┤Ć╔┤╔ó­čĺô...**"
    )


@Client.on_message(commandpro(["/resume", "resume"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await clientbot.pytgcalls.resume_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://te.legra.ph/file/8551742273ea3c66f1ccc.jpg", 
                             caption="**ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í ╔┤ß┤Ćß┤í ╩Çß┤çsß┤ťß┤Źß┤çß┤ů ß┤äß┤ť╩Ç╩Çß┤ç╔┤ß┤Ť╩č╩Ć ß┤ś╩čß┤Ç╩Ć╔¬╔┤╔ó sß┤Ć╔┤╔ó­čĺô...**"
    )



@Client.on_message(commandpro(["/skip", "/next", "skip", "next"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("**ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í ╔┤ß┤Ćß┤Ť╩ť╔¬╔┤╔ó ß┤ś╩čß┤Ç╩Ć╔¬╔┤╔ó ß┤Ç sß┤Ć╔┤╔ó­čśÂ...**")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await clientbot.pytgcalls.leave_group_call(chat_id)
        else:
            await clientbot.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        clientbot.queues.get(chat_id)["file"],
                    ),
                ),
            )


    await message.reply_photo(
                             photo="https://te.legra.ph/file/54a471419fed755bef189.jpg", 
                             caption=f'**ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í sß┤őß┤ő╔¬ß┤śß┤çß┤ů ß┤äß┤ť╩Ç╩Çß┤ç╔┤ß┤Ť╩č╩Ć ß┤ś╩čß┤Ç╩Ć╔¬╔┤╔ó sß┤Ć╔┤╔ó­čśŐ...**'
   ) 


@Client.on_message(commandpro(["/end", "end", "/stop", "stop", "x"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        clientbot.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await clientbot.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_photo(
                             photo="https://te.legra.ph/file/d489e1e2029636319c960.jpg", 
                             caption="**ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í ß┤Źß┤ťs╔¬ß┤ä sß┤Ťß┤Ćß┤Ćß┤śß┤çß┤ů ß┤ś╩čß┤Ç╩Ć╔¬╔┤╔ó..╔¬╔┤ ß┤áß┤Ć╔¬ß┤äß┤ç ß┤ä╩ťß┤Çß┤Ť­čśç..**"
    )


@Client.on_message(commandpro(["/reload", "/refresh"]))
@errors
@authorized_users_only
async def admincache(client, message: Message):
    set(
        message.chat.id,
        (
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ),
    )

    await message.reply_photo(
                              photo="https://te.legra.ph/file/18122c6a3d91ea12feb62.jpg",
                              caption="**ß┤Ťß┤çß┤Çß┤Ź s╩ťß┤Çß┤ůß┤Ćß┤í ß┤Źß┤ťs╔¬ß┤ä sß┤ťß┤äß┤äß┤çssĎôß┤ť╩č╩č╩Ć ╩Çß┤ç╩čß┤Ćß┤Çß┤ůß┤çß┤ů ­čÖé..**"
    )
