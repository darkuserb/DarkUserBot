import asyncio
from telethon import events
from userbot import BRAIN_CHECKER, WHITELIST
from userbot.events import register

@register(incoming=True, from_users=BRAIN_CHECKER, pattern="^.updateall$")
@register(incoming=True, from_users=WHITELIST, pattern="^.updateall$")
async def start(event):
    await event.reply('.update now')
