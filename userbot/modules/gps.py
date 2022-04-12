from geopy.geocoders import Nominatim
from telethon.tl import types

from userbot.events import register
from userbot.cmdhelp import CmdHelp

@register(pattern=r"^.gps (.*)")
async def gps(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("`Boss'a Bir Bölgənin Adını Verməzsən Tapammaz.`")

    await event.edit("**Tapıram...**")

    geolocator = Nominatim(user_agent="iOS")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.reply(
            input_str,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            reply_to=reply_to_id,
        )
        await event.delete()
    else:
        await event.edit("`Üzr İstəyirəm Bu Bölgəyi Tapammadım Şey Xəta Etmiş Olabilərsən :(`")

Help = CmdHelp('gps')
Help.add_command('gps <yer>',  None, ' Dediyin Bölgənin Konumunu Göstərir.').add()
