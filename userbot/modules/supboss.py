from userbot import (BOSS_VERSION, SUPPORT, ASISTAN)
@register(incoming=True, from_users=SUPPORT, pattern="^.clive$",disable_errors=True)
@register(asistan=True, pattern="^.alive$",disable_errors=True)
async def asistanalive(ups):
    bana = await bana_mi_diyo(ups)
    if not bana:
        return
    if ups.sender_id == 5161984781:
        hitap = "💝 ʕっ•ᴥ•ʔっ Asistan"
    else:
        versia = "**Boss V1.0**"
    BossVer = str(BOSS_VERSION.replace("v","")) 
    await ups.reply(f"**Narahat olma admin, mən** {versia} **istifadə edirəm.**")
