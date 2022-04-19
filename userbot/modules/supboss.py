@register(incoming=True, from_users=SUPPORT, pattern="^.clive$",disable_errors=True)   
    if:
        version = "**Boss V1.0**"
    BossVer = str(BOSS_VERSION.replace("v","")) 
    await ups.reply(f"**Narahat olma admin. Mən** {version} istifadə**edirəm.**")
