import asyncio
from telethon import events
from userbot import BRAIN_CHECKER, WHITELIST
from userbot.events import register

@register(incoming=True, from_users=BRAIN_CHECKER, pattern="^.upall$")
@register(incoming=True, from_users=WHITELIST, pattern="^.upall$")
async def start(event):
    await event.reply('.update now')
