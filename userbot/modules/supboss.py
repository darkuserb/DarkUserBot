import asyncio
from telethon import events
from userbot import BRAIN_CHECKER, SUPPORT
from userbot.events import register

@register(incoming=True, from_users=BRAIN_CHECKER, pattern="^.clive$")
@register(incoming=True, from_users=WHITELIST, pattern="^.clive$")
async def start(event):
    await event.reply('`blaj <3`')
