import asyncio
from telethon import events
from userbot import BRAIN_CHECKER, WHITELIST
from userbot.events import register

@register(incoming=True, from_users=BRAIN_CHECKER, pattern="^.husnu$")
@register(incoming=True, from_users=WHITELIST, pattern="^.husnu$")
async def start(event):
    await event.reply('Hüsnü gəlib xoş gəlib')
