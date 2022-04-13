import json
import urllib.request
from userbot.events import register 
from userbot.cmdhelp import CmdHelp 

@register(outgoing=True, pattern=".ipmelumat (.*)") 
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    adress = input_str
    token = "19e7f2b6fe27deb566140aae134dec6b" 
    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1" 

    result = urllib.request.urlopen(api).read()
    result = result.decode()
# siteye göre ayarlı
    result = json.loads(result)
    a = result["type"] 
    b = result["country_code"]
    c = result["region_name"]
    d = result["city"]
    e = result["zip"]
    f = result["latitude"]
    await event.edit("**Verdiyiniz ip adresindən məlumatları axtarıram...** 👀")
    await event.edit(
        f"<b><u>Boss UserBot Modulu</b></u>\n\n<b>IP tipi :-</b><code>{a}</code>\n<b>Ölkə kodu:- </b> <code>{b}</code>\n<b>Dövlət adı :-</b><code>{c}</code>\n<b>Şəhər adı :- </b><code>{d}</code>\n<b>Posta kodu :-</b><code>{e}</code>\n<b>Adres koordinatı:- </b> <code>{f}</code>",
        parse_mode="HTML")

CmdHelp("ipmelumat").add_command('ipmelumat', "{IP adress yazin}", "yazdığınız ip adressinə görə yer təsbiti edər.").add()
