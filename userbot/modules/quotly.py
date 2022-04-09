import datetime

from telethon import events

from telethon.errors.rpcerrorlist import YouBlockedUserError

from telethon.tl.functions.account import UpdateNotifySettingsRequest

from userbot import bot, CMD_HELP

from userbot.events import register


@register(outgoing=True, pattern="^.q(?: |$)(.*)")


async def _(event):

    if event.fwd_from:

        return 

    if not event.reply_to_msg_id:

       await event.edit("```Herhangi bir kullanıcı mesajını yanıtlayın.```")

       return

    reply_message = await event.get_reply_message() 

    if not reply_message.text:

       await event.edit("```Metin mesajını yanıtla```")

       return

    chat = "@QuotLyBot"

    sender = reply_message.sender

    if reply_message.sender.bot:

       await event.edit("```Gerçek kullanıcı mesajını yanıtlayın.```")

       return

    await event.edit("```Alıntı Yapmak```")

    async with bot.conversation(chat) as conv:

          try:     

              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))

              await bot.forward_messages(chat, reply_message)

              response = await response 

          except YouBlockedUserError: 

              await event.reply("```Lütfen @QuotLyBot'un engellemesini kaldırın ve tekrar deneyin```")

              return

          if response.text.startswith("Hi!"):

             await event.edit("```İleriye dönük gizlilik ayarlarınızı nazikçe devre dışı bırakır mısınız?```")

          else: 

             await event.delete()   

             await bot.forward_messages(event.chat_id, response.message)
            
