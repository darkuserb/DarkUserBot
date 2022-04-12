from userbot.cmdhelp import CmdHelp
from userbot import PLUGIN_CHANNEL_ID, CMD_HELP
from userbot.events import register
from re import search
from json import loads, JSONDecodeError
from userbot.language import LANGUAGE_JSON
from os import remove

@register(outgoing=True, pattern="^.dil ?(.*)")
@register(outgoing=True, pattern="^.lang ?(.*)")
async def dil(event):
    global LANGUAGE_JSON

    komut = event.pattern_match.group(1)
    if search(r"y[uü]kle|install", komut):
        await event.edit("`Dil faylı yüklənir...`")
        if event.is_reply:
            reply = await event.get_reply_message()
            dosya = await reply.download_media()

            if ((len(reply.file.name.split(".")) >= 2) and (not reply.file.name.split(".")[1] == "sirijson")):
                return await event.edit("`Xahiş keçərli bir` **BossJSON** `faylı verin!`")

            try:
                dosya = loads(open(dosya, "r").read())
            except JSONDecodeError:
                return await event.edit("`Xahiş keçərli bir` **BossJSON** `faylı verin!`")

            await event.edit(f"`{dosya['LANGUAGE']}` `dili yüklənir...`")
            pchannel = await event.client.get_entity(PLUGIN_CHANNEL_ID)

            dosya = await reply.download_media(file="./userbot/language/")
            dosya = loads(open(dosya, "r").read())
            await reply.forward_to(pchannel)
            
            LANGUAGE_JSON = dosya
            await event.edit(f"✅ `{dosya['LANGUAGE']}` `dili Uğurla yüklendi!`\n\n**İşləmlərin keçərli olması üçün botu yenidən başladın!**")
        else:
            await event.edit("**Xahiş bir dil faylına yanıt verin!**")
    elif search(r"məlumat|info", komut):
        await event.edit("`Dil faylı məlumatları gətirilir... Xahiş gözlə.`")
        if event.is_reply:
            reply = await event.get_reply_message()
            if ((len(reply.file.name.split(".")) >= 1) and (not reply.file.name.split(".")[1] == "sirijson")):
                return await event.edit("`Xahiş keçərli bir` **BossJSON** `faylı verin!`")

            dosya = await reply.download_media()

            try:
                dosya = loads(open(dosya, "r").read())
            except JSONDecodeError:
                return await event.edit("`Xahiş keçərli bir` **BodsJSON** `faylı verin!`")

            await event.edit(
                f"**Dil: **`{dosya['LANGUAGE']}`\n"
                f"**Dil Kodu: **`{dosya['LANGCODE']}`\n"
                f"**Çevirmen: **`{dosya['AUTHOR']}`\n"

                f"\n\n`Dil faylını yükləmək üçün` `.dil yükle` `yazın`"
            )
        else:
            await event.edit("**Lütfen bir dil faylına yanıt verin!**")
    else:
        await event.edit(
            f"**🪙 Dil: **`{LANGUAGE_JSON['LANGUAGE']}`\n"
            f"**🔋 Dil Kodu: **`{LANGUAGE_JSON['LANGCODE']}`\n"
            f"**⌨️ Çeviren: **`{LANGUAGE_JSON ['AUTHOR']}`\n"
        )

CmdHelp('dil').add_command(
    'dil', None, 'Yüklədiyiniz dil haqqında məlumat verir.'
).add_command(
    'dil məlumat', None, 'Yanıt verdiyiniz dil faylı haqqında məlumat verir.'
).add_command(
    'dil yükle', None, 'Yanıt verdiyiniz dil faylını yüklüyər.'
).add()
