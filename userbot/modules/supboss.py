@register(incoming=True, from_users=WHITELIST, pattern="^.wlive$",disable_errors=True)
@register(asistan=True, pattern="^.alive$",disable_errors=True)
async def asistanalive(ups):
    bana = await bana_mi_diyo(ups)
    if not bana:
        return
    if ups.sender_id == 5161984781:
        hitap = "💝 ʕっ•ᴥ•ʔっ Asistan"
    else:
        hitap = "Yöneticim"
    SiriVer = str(BOSS_VERSION.replace("v","")) 
    await ups.reply(f"__{hitap} səni sevirəm❤! Boss işləyir!__")
