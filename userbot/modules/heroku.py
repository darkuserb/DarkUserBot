import codecs
import heroku3
import asyncio
import aiohttp
import math
import os
import ssl
import requests

from userbot import (
    HEROKU_APPNAME,
    HEROKU_APIKEY,
    BOTLOG,
    ASISTAN,
    DangerousSubstance,
    MYID,
    BOTLOG_CHATID
)

from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot.helps.asistan import bana_mi_diyo
from telethon.errors.rpcerrorlist import PeerIdInvalidError # Botlog grubundan çıktıysa


heroku_api = "https://api.heroku.com"
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None:
    Heroku = heroku3.from_key(HEROKU_APIKEY)
    app = Heroku.app(HEROKU_APPNAME)
    heroku_var = app.config()
else:
    app = None
    heroku_var = None

"""Config Vars değeri ilave edin veya silin..."""


@register(outgoing=True, pattern=r"^.(get|del) var(?: |$)(\w*)")
async def variable(var):
    exe = var.pattern_match.group(1)
    if app is None:
        await var.edit("`[HEROKU]"
                       "\n**HEROKU_APPNAME** Yükleyin.")
        return False
    if exe == "get":
        await var.edit("`🔄 Heroku Məlumaları Gətirilir..`")
        variable = var.pattern_match.group(2)
        if variable != '':
            if variable in heroku_var:
                if BOTLOG:
                    await var.client.send_message(
                        BOTLOG_CHATID, "#CONFIGVAR\n\n"
                        "**ConfigVar**:\n"
                        f"`{variable}` = `{heroku_var[variable]}`\n"
                    )
                    await var.edit("`BOTLOG grubuna gönderdim!`")
                    return True
                else:
                    await var.edit("`Lütfen BOTLOG grubu ayarlayınız...`")
                    return False
            else:
                await var.edit("`Xəta:` **Olmayan Bir dəyər dəyiştiriləməz.**")
                return True
        else:
            configvars = heroku_var.to_dict()
            if BOTLOG:
                msg = ''
                for item in configvars:
                    if item in DangerousSubstance:
                        continue
                    msg += f"`{item}` = `{configvars[item]}`\n"
                await var.client.send_message(
                    BOTLOG_CHATID, "#CONFIGVARS\n\n"
                    "**ConfigVars**:\n"
                    f"{msg}"
                
                await var.edit("`BOTLOG_CHATID alındı...`")
                return True
            else:
                await var.edit("`Xahiş BOTLOG'u True olaraq ayarlayın!`")
                return False
    elif exe == "del":
        await var.edit("`Məlumatları silirəm...`")
        variable = var.pattern_match.group(2)
        if variable == '':
            await var.edit("`Silmək istədiyiniz ConfigVars'ı seçin və mənə bildirin...`")
            return False
        if variable in heroku_var:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#DELCONFIGVAR\n\n"
                    "**ConfigVar Silindi**:\n"
                    f"`{variable}`"
                )
            await var.edit("`məlumatlar silindi!`")
            del heroku_var[variable]
        else:
            await var.edit("`Məlumatlar Yoxdur!`")
            return True


@register(pattern=r'^.set var (\w*) ([\s\S]*)')
async def set_var(var):
    await var.edit("`🔄 Verilənlər Herokuya Yazılır...`")
    variable = var.pattern_match.group(1)
    value = var.pattern_match.group(2)
    fix = False
    if variable in heroku_var:
        try:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#SETCONFIGVAR\n\n"
                    "**ConfigVar Değişikliği**:\n"
                    f"`{variable}` = `{value}`"
                )
            await var.edit(f"`✅ {variable} dəyəri dəyiştirildi!`")
        except:
             fix = True
             await var.edit("😒 Botlog grubundan çıxmısan.. Sənin üçün düzəldirəm..")
    else:
        try:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#ADDCONFIGVAR\n\n"
                    "**Yeni ConfigVar Eklendi**:\n"
                    f"`{variable}` = `{value}`"
                )
            await var.edit(f"`✅ {variable} dəyəri ayarlandı!`")
        except Exception:
            fix = True
            await var.edit("😒 Botlog grubundan çıxmısan.. Sənin üçün düzəldirəm..")
    if fix:
        heroku_var["BOTLOG"] = "False"
        heroku_var["BOTLOG_CHATID"] = "0"
    else:
        heroku_var[variable] = value


#@register(asistan=True, pattern="^.setvar (\w*) ([\s\S]*)")
async def asistansetvar(ups):
    """ Sadece bilgileri değiştirebilir kodlardan görüldüğü üzere bilgileri göremez. """
    bana = await bana_mi_diyo(u)
    if not bana:
        return
    usp = await ups.reply("`⚙️ Asistan'dan alınan datalar herokuya yazılır...`")
    dg = ups.text.replace(".setvar ","")
    dgs = dg.split(":")
    variable = dgs[0]
    value = dgs[1]
    if variable in heroku_var:
        if BOTLOG:
            await ups.client.send_message(
                BOTLOG_CHATID, "#SETCONFIGVAR\n\n"
                "**Asistan tarafından ConfigVar Değişikliği**:\n"
                f"`{variable}` = `{value}`"
            )
    else:
        if BOTLOG:
            await ups.client.send_message(
                BOTLOG_CHATID, "#ADDCONFIGVAR\n\n"
                "**Yeni ConfigVar Eklendi**:\n"
                f"`{variable}` = `{value}`"
            )
    await usp.edit("`⚙️ Asistandan alınan datalar herokuya axtarıldı!`")
    heroku_var[variable] = value


"""Hesabınızdakı dynosuna bakmanızı yarayan userbot modulu"""


@register(pattern=r"^.dyno(?: |$)")
async def dyno_usage(dyno):
    """Bu qisimdə bot istifadə edilmiş dynonu əldə etməyə çalışır"""
    await dyno.edit("`🔄 Xahiş Gözləyin...`")
    useragent = ('Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/80.0.3987.149 Mobile Safari/537.36'
                 )
    u_id = Heroku.account().id
    headers = {
     'User-Agent': useragent,
     'Authorization': f'Bearer {HEROKU_APIKEY}',
     'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
    }
    path = "/accounts/" + u_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("`Error: something bad happened`\n\n"
                               f">.`{r.reason}`\n")
    result = r.json()
    quota = result['account_quota']
    quota_used = result['quota_used']

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    remaining = math.floor(hours / 24) # Sadece şu satır için eyw @coshgyn

    """ - Current - """
    App = result['apps']
    try:
        App[0]['quota_used']
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]['quota_used'] / 60
        AppPercentage = math.floor(App[0]['quota_used'] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await dyno.edit("**✨ Qalan Dyno**:\n\n"
                           f" 👉🏻 `İşlədilən Dyno Saati`  **({HEROKU_APPNAME})**:\n"
                           f"     ⌛  `{AppHours}` **saat**  `{AppMinutes}` **dakika**  "
                           f"**|**  [`{AppPercentage}` **%**]"
                           "\n"
                           " 👉🏻 `Bu ay üçün qalan dyno saatı`:\n"
                           f"     ⌛  `{hours}` **saat**  `{minutes}` **dakika**  "
                           f"**|**  [`{percentage}` **%**]\n"
                           " 👉🏻 `Nə zaman bitər`:\n"
                           f"      ⌛  [**{remaining} gün**]"
                           )

@register(pattern=r"^.herokulog")
async def herokulog(dyno):
    try:
        Heroku = heroku3.from_key(HEROKU_APIKEY)
        app = Heroku.app(HEROKU_APPNAME)
    except BaseException:
        return await dyno.reply(
            "`Xahiş Gözləyin ,Heroku VARS'da Heroku API Key və Heroku APP name'in düzgün olduğundan əmin olun.`"
        )
    await dyno.edit("`🔄 Log gətirilir....`")
    with open("logs.txt", "w") as log:
        log.write(app.get_log())
    fd = codecs.open("logs.txt", "r", encoding="utf-8")
    data = fd.read()
    key = (requests.post("https://nekobin.com/api/documents",
                         json={"content": data}) .json() .get("result") .get("key"))
    url = f"https://nekobin.com/raw/{key}"
    await dyno.edit(f"`Heroku log'u :`\n\n: [S  İ  R  İ]({url})")
    return os.remove("logs.txt")


CmdHelp('heroku').add_command(
'dyno', None, 'Dyno saatı haqqında məlumat verir..'
    ).add_command(
        'set var', None, 'set var <Yeni Var adı> <dəyər> Botunuza yeni ConfigVar salır.'
    ).add_command(
        'get var', None, 'Mövcud VARlarınızı əldə edin, yalnızca botlog gurubunuzda tapa bilərsiniz .'
    ).add_command(
        'del var', None, 'del var <Var adı> Seçdiyiniz ConfigVarı silər sildiktən sonra botunuza .restart atın.'
    ).add_command(
        'log', None, 'Heroku logunuza baxın'
    ).add_info(
        '**Botlog grubundan çıxsanız sizin yerinizə düzəltməsi üçün** `.set var BOTLOG False` **yazın.. ✨**'
    ).add()
