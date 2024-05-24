import random
import re
import time
from platform import python_version
import os
from telethon import version, Button, events
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from BlackThonUB import StartTime, BlThon, JEPVERSION

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import mention

plugin_category = "utils"

@BlThon.on(events.NewMessage(pattern='.event', outgoing=True))
async def my_event_handler(event):
    if event.is_reply:
        replied_message = await event.get_reply_message()
        if replied_message:
            event_info = replied_message
            with open("event_info.txt", "w") as file:
                file.write(event_info.stringify())
            await BlThon.send_file(event.chat_id, "event_info.txt")
            os.remove("event_info.txt")

@BlThon.ar_cmd(
    pattern="المطور$",
    command=("المطور", plugin_category),
    info={
        "header": "لأظهار مطورين السورس",
        "usage": [
            "{tr}المطور",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  - "
    CUSTOM_ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    CAT_IMG = "https://j.top4top.io/p_30669tgy70.jpg"
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption = f"مطورين بـلاكـثون\n"
        cat_caption += f"✛━━━━━━━━━━━━━✛\n"
        cat_caption += f"- المطور  : @abx7e\n"
        cat_caption += f"- المطور  : @abs7e\n"
        cat_caption += f"✛━━━━━━━━━━━━━✛\n"
        await event.client.send_file(
            event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id
        )

@BlThon.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)

progs = [6013286715]

@BlThon.on(events.NewMessage(incoming=True))
async def reda(event):
    if event.reply_to and event.sender_id in progs:
       reply_msg = await event.get_reply_message()
       owner_id = reply_msg.from_id.user_id
       if owner_id == BlThon.uid:
           if event.message.message == "حظر من السورس":
               await event.reply("**حاظر مطوري ، لقد تم حظره من استخدام السورس**")
               addgvar("blockedfrom", "yes")
           elif event.message.message == "الغاء الحظر من السورس":
               await event.reply("**حاظر مطوري، لقد الغيت الحظر**")
               delgvar("blockedfrom")
                

