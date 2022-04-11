import asyncio
from telethon import events
from userbot import BRAIN_CHECKER, WHITELIST
from userbot.events import register

@register(incoming=True, from_users=BRAIN_CHECKER, pattern="^.blive$")
@register(incoming=True, from_users=WHITELIST, pattern="^.blive$")
async def _(q):
    await q.client.send_message(q.chat_id,"`ㅤ  ☾︎ㅤ✨ẞ𝙾𝚂𝚂 𝚄𝚜𝚎𝚛𝚋𝚘𝚝ㅤ✨☽︎  `")
