from telethon import events
from BlackThonUB import *
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete
from telethon import functions
from telethon.errors.rpcerrorlist import MessageIdInvalidError
@BlThon.on(admin_cmd(pattern="(خط الغامق|خط غامق)"))
async def btext(event):
    isbold = gvarstatus("bold")
    if not isbold:
        addgvar ("bold", "on")
        await edit_delete(event, "**᯽︙ تم تفعيل خط الغامق بنجاح ✓**")
        return

    if isbold:
        delgvar("bold")
        await edit_delete(event, "**᯽︙ تم اطفاء خط الغامق بنجاح ✓ **")
        return

@BlThon.on(admin_cmd(pattern="(خط المشطوب|خط مشطوب)"))
async def btext(event):
    istshwesh = gvarstatus("tshwesh")
    if not istshwesh:
        addgvar ("tshwesh", "on")
        await edit_delete(event, "**᯽︙ تم تفعيل خط المشطوب بنجاح ✓**")
        return

    if istshwesh:
        delgvar("tshwesh")
        await edit_delete(event, "**᯽︙ تم اطفاء خط المشطوب بنجاح ✓ **")
        return

@BlThon.on(admin_cmd(pattern="(خط رمز|خط الرمز)"))
async def btext(event):
    isramz = gvarstatus("ramz")
    if not isramz:
        addgvar ("ramz", "on")
        await edit_delete(event, "**᯽︙ تم تفعيل خط الرمز بنجاح ✓**")
        return

    if isramz:
        delgvar("ramz")
        await edit_delete(event, "**᯽︙ تم اطفاء خط الرمز بنجاح ✓ **")
        return

@BlThon.on(admin_cmd(pattern="(خط بـلاكـثون|خط جوكر)"))
async def AlBlackThon(event):
    AlBlackThon = gvarstatus("BlackThon")
    if not AlBlackThon:
        addgvar ("BlackThon", "on")
        await edit_delete(event, "**᯽︙ تم تفعيل خط بـلاكـثون بنجاح ✓**")
        return

    if AlBlackThon:
        delgvar("بـلاكـثون")
        await edit_delete(event, "**᯽︙ تم اطفاء خط بـلاكـثون بنجاح ✓ **")
        return

@BlThon.on(events.NewMessage(outgoing=True))
async def reda(event):
    if event.message.text and not event.message.media and event.message.text.count(".") != 1 and event.message.text.count("@") != 1 and event.message.text.count("/") != 1:
        isbold = gvarstatus("bold")
        isramz = gvarstatus("ramz")
        istshwesh = gvarstatus("tshwesh")
        AlBlackThon = gvarstatus("BlackThon")
        if isbold:
            try:
                await event.edit(f"**{event.message.text}**")
            except MessageIdInvalidError:
                pass
        if isramz:
            try:
                await event.edit(f"`{event.message.text}`")
            except MessageIdInvalidError:
                pass
        if istshwesh:
            try:
                await event.edit(f"~~{event.message.text}~~")
            except MessageIdInvalidError:
                pass
        if AlBlackThon:
            try:
                await event.edit(f"```{event.message.text}```")
            except MessageIdInvalidError:
                pass
