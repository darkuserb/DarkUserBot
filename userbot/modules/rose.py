# SİRİ USERBOT - PLUGİN

import os
from telethon.errors import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.cmdhelp import CmdHelp

chat = "@MissRose_bot"

@register(outgoing=True, pattern="^.fstat ?(.*)")
async def fstat(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fedstat " + kullanıcı + " " + siri)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot' Bloklanmışdır Yenidən Başladın Təkrar edin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fedstat " + siri)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot' Bloklanmışdır Başladın Təkrar edin.")


@register(outgoing=True, pattern="^.info ?(.*)")
async def info(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
        
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/info " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yenidən Başladın Təkrar edin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/info " + siri)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yenidən Başladın Təkrar Edin.")


@register(outgoing=True, pattern="^.fedinfo ?(.*)")
async def fedinfo(event):
    if event.fwd_from:
        return
    siri = event.pattern_match.group(1)
    if siri == "" and not event.reply_to_msg_id:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fedinfo")
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yenidən Başladın Təkrar Edin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fedinfo " + siri)
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yenidən Başladın Təkrar Edin.")


@register(outgoing=True, pattern="^.myfeds ?(.*)")
async def myfeds(event):
    if event.fwd_from:
        return
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/myfeds")
            myfed = await conv.get_response()
            if "file" in myfed.text:
                await fedstat.click(0)
                reply = await conv.get_response()
                await event.client.send_message(event.chat_id, reply)
            else:
                await event.client.send_message(event.chat_id, myfed)
                await event.delete()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("@MissRose_bot'u Yenidən Başladın Təkrar Edin.")
            
@register(outgoing=True, pattern="^.fban ?(.*)")
async def fban(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
        
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fban " + kullanıcı)
                audio = await conv.get_response()
                n.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fban " + siri)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yenidən Başladın Təkrar Edin.")
                
@register(outgoing=True, pattern="^.unfban ?(.*)")
async def unfban(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
        
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/unfban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yenidən Başladın Təkrar Edin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/unfban " + siri)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yenidən Başladın Təkrar Edin.")
                
@register(outgoing=True, pattern="^.feddemote ?(.*)")
async def feddemote(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
        
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/feddemote " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yenidən Başladın Təkrar Edin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/unfban " + siri)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yenidən Başladın Təkrar Edin.")
                
@register(outgoing=True, pattern="^.fpromode ?(.*)")
async def fpromode(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        siri = event.pattern_match.group(1)
        
    else:
        siri = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fpromode " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yenidən Başladın Təkrar Edin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/fpromode " + siri)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u Yeniden Başlatın Tekrar Deneyin.")
            
CmdHelp('rose').add_command(
    'fstat', '<tag/id>', 'Sadəcə .fstat Yazarsanız özünüz Üçün Fban Listini Verir. \n ID vəya @KULLANICI ADI Versəniz O User Fban Listini Verir '
).add_command(
    'info', '<tag/id>', 'Sadəcə .info Yazsanız özünüz üçün Məlumat verir. \n ID vəya @KULLANICI ADI Versəniz O Usee Üçün Məlumat Verir.'
).add_command(
    'fedinfo', '<fed id>', 'Sadəcə .fedinfo yazsanız Sizin Federasiyanız Üçün Məlumat Verir. \n FED İD Girərsəniz O Federasiyanın Məlumatını Verir'
).add_command(
    'myfeds', 'Hangi Federasiyalardan Yetkinizin Olduğunu Göstərir.'
).add_command(
    'fban', '<tag/id>', 'Bunu Federasiya Sahibləri İşlədə Bilir.\n Tapıldığınız Gruptaki Userə öz Federasiyanızdan Fban ata bilərsiniz. '
).add_command(
    'unfban', '<tag/id>', ' Bunu Federasiya Sahibləri İşlədə Bilir.\n Tapıldığınız Gruptaki Userə öz Federasiyanızdan Fbanını Aça bilərsiniz. '
).add_command(
    'fpromote', '<tag/id>', ' Bunu Federasiya Sahibləri İşlədə Bilir.\n Tapıldığınız Gruptaki Userə öz Federasiyanızdan Fban Yetkisi Verəbilərsiniz. '
).add_command(
    'feddemote', '<tag/id>', ' Bunu Federasyon Sahipleri Kullana Bilir.\n Tapıldığınız Gruptaki Userə öz Federasiyanızdan Fban yetkisini Alabilərsiniz. : 'Bu əmrlər hər yerdə işləməyə bilər Özəl mesajlarda yaxud qruplarda işləyə bilər @BossUserBot '
    
).add()
