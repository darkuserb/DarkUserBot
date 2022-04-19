@register(incoming=True, from_users=WHITELIST, pattern="^.wlive$",disable_errors=True)   
    else:
        version = "**Boss V1.0**"
    BossVer = str(BOSS_VERSION.replace("v","")) 
    await ups.reply(f"**Narahat olma admin. Mən** {version} istifadə**edirəm.**")
