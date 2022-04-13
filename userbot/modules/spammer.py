# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# SiriUserBot - ErdemBey - Berceste - Midy


import asyncio
import threading

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.tspam")
async def tmeme(e):
    message = e.text
    messageSplit = message.split(" ", 1)
    tspam = str(messageSplit[1])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()
    if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#TSPAM \n\n"
                "TSpam Uğurla gerçəkləştirildi"
                )

@register(outgoing=True, pattern="^.spam")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit = message.split(" ", 2)
        counter = int(messageSplit[1])
        spam_message = str(messageSplit[2])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#SPAM \n\n"
                "Spam Uğurla gerçəkləştirildi"
                )
                               
@register(outgoing=True, pattern="^.bigspam")
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit = message.split(" ", 2)
        counter = int(messageSplit[1])
        spam_message = str(messageSplit[2])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#BIGSPAM \n\n"
                "Bigspam başarıyla gerçekleştirildi"
                )
        
        
@register(outgoing=True, pattern="^.picspam")
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        link = str(text[2])
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, link)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#PICSPAM \n\n"
                "PicSpam Uğurla gerçəkləştirildi"
                )


@register(outgoing=True, pattern="^.delayspam")
async def delayspammer(e):
    # Teşekkürler @ReversedPosix
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit= message.split(" ", 3)
        spam_delay = float(messageSplit[1])
        counter = int(messageSplit[2])
        spam_message = str(messageSplit[3])
        await e.delete()
        delaySpamEvent = threading.Event()
        for i in range(1, counter):
            await e.respond(spam_message)
            delaySpamEvent.wait(spam_delay)
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#DelaySPAM \n\n"
                "DelaySpam Uğurla gerçələştirildi"
                )

@register(outgoing=True, pattern="^.mspam(?: |$)(.*)")
async def media_spam(event):
    if event.fwd_from:
        return
    
    cmd = event.pattern_match.group(1)
    if len(cmd) < 1:
        await event.edit("`Xahiş bir sayı deyin! Nümunə: .mspam 10`") 
        return
    elif not cmd.isdigit():
        await event.edit("`Xahiş sadəcə sayı deyin! Nümunə: .mspam 10`") 
        return
    replymsg = await event.get_reply_message()
    if not event.reply_to_msg_id or not replymsg.media:
        await event.edit("`Xahiş bir medyaya yanıt verin. Bu səs, musiqi, şəkil, sticker, gif, video ola bilər.`") 
        return
    
    i = 0
    await event.delete()
    while i < int(cmd):
        await event.respond(replymsg)
        await asyncio.sleep(0.1)
        i += 1
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#MedyaSPAM \n\n"
            "MedyaSpam Uğurla gerçəkləştirildi"
            )





CmdHelp('spammer').add_command(
    'tspam', '<mətin>', 'Verilən mesajı tək tək göndərərək spam edər.'
).add_command(
    'spam', '<miqdar> <mətin>', 'Verilən miqdarda spam göndərir.'
).add_command(
    'bigspam', '<miqdar> <mətin>', 'Verilən miqdarda spam göndərir.'
).add_command(
    'picspam', '<miqdar> <link>', 'Verilən miqdarda rəsimli spam göndərir.'
).add_command(
    'mspam', '<miqdar> <yanıtladığınız medya>', 'Verilən miqdar qədər yanıt verdiyiniz şəkil/musiqi/səs/video spamı edər.'
).add_command(
    'delayspam', '<gecikmə> <miqdar> <mətin>', 'Verilən miqdar və verilən gecikmə ilə gecikməli spam edər.'
).add_command(
    'kill spam', None, "Spam durdurma", None
).add_warning(
    'Məsuliyyət sizin üstünüzdədir!!'
).add()
