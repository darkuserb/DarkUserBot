from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot import bot

@register(outgoing=True, pattern="^.endir ?(.*)")
async def bossinsta(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Yükləmək üçün Link Verin`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Yükləmək üçün Link Verin`")
        return
    chat = "@SaveAsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Boss Endirmədi Bəzi Xətalar Nədəniylə Başqa Link Cəhd et Də Ürəyim ✓`")
        return
    asc = await event.edit("`Boss Yükləyir Səbirli Ol...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit(" @SaveAsBot `botunun Blokunu Qaldırın Təkrar Cəhd edin")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "`Gizlilik ayarlarınızdakı mesaj qismini düzəldin.`"
            )
        elif "Что поддерживается?" in response.text:
            await event.edit(
                "⛔️ `Bu linkin nə olduğu haqqında bir fikrim yoxdu!`"
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"@BossUserBot `ilə yükləndi`",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            

CmdHelp('endir').add_command(
    'endir', None, 'Linki Yanıtlayın .indir əmri İlə\nİnstagramdan IGTV-Hikaye-Video-Şəkil\nTikTokdan Video\nPinteresttən Video-Şəkil'
).add()
