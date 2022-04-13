# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# SiriUserBot - Berceste


""" Birkaç küçük komutu içeren UserBot modülü. """

from random import randint
from time import sleep
from os import execl
import sys
import io
from userbot import BOTLOG, BOTLOG_CHATID, ASISTAN, MYID, CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("misc")

# ████████████████████████████████ #

@register(pattern="^.resend")
async def resend(event):
    await event.delete()
    m = await event.get_reply_message()
    if not m:
        event.edit(LANG['REPLY_TO_FILE'])
        return
    await event.respond(m)

@register(pattern="^.random")
async def randomise(items):
    """ .random komutu, eşya listesinden rastgele bir eşya seçer. """
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            LANG['NEED_MUCH_DATA_FOR_RANDOM']
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit(f"**{LANG['QUERY']}: **\n`" + items.text[8:] + f"`\n**{LANG['RESULT']}: **\n`" +
                     itemo[index] + "`")


@register(pattern="^.sleep( [0-9]+)?$")
async def sleepybot(time):
    """ .sleep komutu Boss'nın birkaç saniye uyumasına olanak sağlar. """
    if " " not in time.pattern_match.group(1):
        await time.reply(LANG['SLEEP_DESC'])
    else:
        counter = int(time.pattern_match.group(1))
        await time.edit(LANG['SLEEPING'])
        sleep(2)
        if BOTLOG:
            await time.client.send_message(
                BOTLOG_CHATID,
                "Botu" + str(counter) + "saniyə yuxuya buraxdın.",
            )
        sleep(counter)
        await time.edit(LANG['GOODMORNIN_YALL'])


@register(pattern="^.shutdown$")
async def shutdown(event):
    """ .shutdown komutu botu kapatır. """
    await event.client.send_file(event.chat_id, 'https://www.winhistory.de/more/winstart/mp3/winxpshutdown.mp3', caption=LANG['GOODBYE_MFRS'], voice_note=True)
    await event.delete()

    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n"
                                        "Bot bağlandı.")
    try:
        await bot.disconnect()
    except:
        pass

@register(asistan=True, pattern="^.shutdown$")
async def asistanshutdown(ups):
    """ .shutdown komutunu asistana söylerseniz sizin yerinize o botu kapatır. """
    if ups.is_reply:
        reply = await ups.get_reply_message()
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == MYID:
            try:
                await event.client.send_file(event.chat_id, 'https://www.winhistory.de/more/winstart/mp3/winxpshutdown.mp3', reply_to=reply, caption=LANG['GOODBYE_MFRS'], voice_note=True)
            except:
                await ups.reply("`Görüşmək üzrə.. İstəyin üzərə özümü bağlıyıram.`") 
            try:
                await bot.disconnect()
            except:
                pass


@register(pattern="^.kill (.*)")
@register(pattern="^.restart$")
async def restart(event):
    await event.edit(LANG['RESTARTING'])
    if BOTLOG:
        try:
            await event.client.send_message(BOTLOG_CHATID, "#RESTART \n"
                                            "Bot yeniden başladıldı.")
        except:
            pass

    try:
        await bot.disconnect()
    except:
        pass

    execl(sys.executable, sys.executable, *sys.argv)

@register(pattern="^.support$")
async def bot_support(wannahelp):
    """ .support komutu destek grubumuzu verir. """
    await wannahelp.edit(LANG['SUPPORT_GROUP'])



@register(pattern="^.creator$")
async def creator(e):
    await e.edit(LANG['CREATOR'])


@register(pattern="^.readme$")
async def reedme(e):
    await e.edit(LANG['README'])


# Copyright (c) Gegham Zakaryan | 2019
@register(pattern="^.repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(' ', 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@register(pattern="^.repo$")
async def repo_is_here(wannasee):
    """ .repo komutunun tek yaptığı şey GitHub repomuzun bağlantısını vermek. """
    await wannasee.edit(LANG['REPO'])

@register(pattern="^.raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit(
            "`Həll olmuş mesaj üçün userbot loglarını yoxla!`")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Həll olan mesaj`")

CmdHelp('misc').add_command(
    'random', '<əşya1> <əşya2> ... <əşyaN>', 'Əşya listəsindəj random bir əşya seçər', 'random boss uniborg userge'
).add_command(
    'sleep', '<vaxt>', 'Boss da bir insan, o da yorulur. Ara sıra biraz yatmasına icazə ver.', 'sleep 30'
).add_command(
    'shutdown', None, 'Nostalji bir şəkildə botunuzu bağlayın.'
).add_command(
    'repo', None, 'Boss botunun GitHub\'daki reposuna gedən bir bağlantı.'
).add_command(
    'readme', None, 'Boss botunun GitHub\'daki README.md faylına gedən bir bağlantı.'
).add_command(
    'creator', None, 'Bu gözəl botu kimlərin yaratdığını öyrən :-)'
).add_command(
    'repeat', '<sayı> <mətin>', 'Bir mətni bəlli bir sayıda təkrar edər. Spam əmri ilə qarıştırma!'
).add_command(
    'restart', None, 'Botu yeniden başlatır.'
).add_command(
    'resend', None, 'Bir medyayı yenidən göndərir.'
).add_command(
    'resend', None, 'Bir medyayı yenidən göndərir.'
).add_command(
    'raw', '<yanıt>', 'Yanıt verilən mesaj haqqında məlumat  verir.'
).add()
