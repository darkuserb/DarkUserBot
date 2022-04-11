import asyncio
from telethon import events
from userbot import BRAIN_CHECKER, WHITELIST
from userbot.events import register

@register(incoming=True, from_users=BRAIN_CHECKER, pattern="^.update all$")
@register(incoming=True, from_users=WHITELIST, pattern="^.update all$")
async def start(event):
    await event.reply('.update now')
