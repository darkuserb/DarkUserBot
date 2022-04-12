

from telethon import events
import asyncio
from userbot.events import register

@register(outgoing=True, pattern="^.yay ?(.*)")
async def yay(event):
    mesaj = event.pattern_match.group(1)
    if len(mesaj) < 1:
        await event.edit("`Birşeyləri Yaymak üçün bir mesaj verməniz lazımdır. Nümunə: ``.yay Salam dünya`")
        return

    if event.is_private:
        await event.edit("`Bu əmr sadəcə gruplarda işləməkdədir.`")
        return

    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await event.edit("`Ciddisən? Admin olmadığın bir grupta duyuru göndərmənə icazə vermiyəcəyəm!`")
        return

    await event.edit("`Tüm üyelerinize duyurunuz gönderiliyor...`")
    all_participants = await event.client.get_participants(event.chat_id, aggressive=True)
    a = 0

    for user in all_participants:
        a += 1
        uid = user.id
        if user.username:
            link = "@" + user.username
        else:
            link = "[" + user.first_name + "](" + str(user.id) + ")"
        try:
            await event.client.send_message(uid, mesaj + "\n\n@SiriUserBot ile gönderildi.")
            son = f"**Son duyuru göndərilən kullanıcı:** {link}"
        except:
            son = f"**Son duyuru gönderilen kullanıcı:** **Göndəriləmədi!**"
    
        await event.edit(f"`Bütün üzvlərinizə duyurunuz göndərilir...`\n{son}\n\n**Durum:** `{a}/{len(all_participants)}`")
        await asyncio.sleep(0.5)

    await event.edit("`Bütün üzvlərinizə duyurunuz göndərildi!`\n\nby @BossUserBot 😙")
