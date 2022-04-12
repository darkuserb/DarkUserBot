# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# SiriUserBot - Berceste
#

''' Gruba katılan spamcıları banlamada yardımcı olan modüldür. '''

from asyncio import sleep
from requests import get

from telethon.events import ChatAction
from telethon.tl.types import ChannelParticipantsAdmins, Message

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, ANTI_SPAMBOT, ANTI_SPAMBOT_SHOUT, BLACKLIST_CHAT, bot


@bot.on(ChatAction)
async def anti_spambot(welcm):
    try:
        ''' Əgər bir user spam algoritmiylə eşleşərsə
           onu gruptan qadağan edər. '''
        if not ANTI_SPAMBOT:
            return
        if isinstance(BLACKLIST_CHAT, list):
            if welcm.chat_id in BLACKLIST_CHAT:
                return
        if welcm.user_joined or welcm.user_added:
            adder = None
            ignore = False
            users = None

            if welcm.user_added:
                ignore = False
                try:
                    adder = welcm.action_message.from_id
                except AttributeError:
                    return

            async for admin in bot.iter_participants(
                    welcm.chat_id, filter=ChannelParticipantsAdmins):
                if admin.id == adder:
                    ignore = True
                    break

            if ignore:
                return

            elif welcm.user_joined:
                users_list = hasattr(welcm.action_message.action, "users")
                if users_list:
                    users = welcm.action_message.action.users
                else:
                    users = [welcm.action_message.from_id]

            await sleep(5)
            spambot = False

            if not users:
                return

            for user_id in users:
                async for message in bot.iter_messages(welcm.chat_id,
                                                       from_user=user_id):

                    correct_type = isinstance(message, Message)
                    if not message or not correct_type:
                        break

                    join_time = welcm.action_message.date
                    message_date = message.date

                    if message_date < join_time:
                        # Eğer mesaj kullanıcı katılma tarihinden daha önce ise yoksayılır.
                        continue

                    check_user = await welcm.client.get_entity(user_id)

                    # Hata ayıklama. İlerideki durumlar için bırakıldı. ###
                    print(
                        f"Katılan kullanıcı: {check_user.first_name} [ID: {check_user.id}]"
                    )
                    print(f"Sohbet: {welcm.chat.title}")
                    print(f"Zaman: {join_time}")
                    print(
                        f"Gönderdiği mesaj: {message.text}\n\n[Zaman: {message_date}]"
                    )
                    ##############################################

                    try:
                        cas_url = f"https://api.cas.chat/check?user_id={check_user.id}"
                        r = get(cas_url, timeout=3)
                        data = r.json()
                    except BaseException:
                        print(
                            "CAS kontrolü başarısız, eski anti_spambot kontrolüne dönülüyor."
                        )
                        data = None
                        pass

                    if data and data['ok']:
                        reason = f"[Combot Anti Spam tərəfindən banlandı.](https://cas.chat/query?u={check_user.id})"
                        spambot = True
                    elif "t.cn/" in message.text:
                        reason = "`t.cn` URL'ləri tapıldı."
                        spambot = True
                    elif "t.me/joinchat" in message.text:
                        reason = "Bacarıq reklam mesajı"
                        spambot = True
                    elif message.fwd_from:
                        reason = "Başqasından ilətilən mesaj"
                        spambot = True
                    elif "?start=" in message.text:
                        reason = "Telegram botu `start` linki"
                        spambot = True
                    elif "bit.ly/" in message.text:
                        reason = "`bit.ly` URL'ləri tapıldı."
                        spambot = True
                    elif "tr.link/" in message.text:
                        reason = "`tr.link` URL'ləri tapıldı."
                        spambot = True
                    elif "ay.live/" in message.text:
                        reason = "`ay.live` URL'ləri tapıldı."
                        spambot = True
                    elif "exe.io/" in message.text:
                        reason = "`exe.io` URL'ləri tapıldı."
                        spambot = True
                    elif "ouo.io/" in message.text:
                        reason = "`ouo.io` URL'ləri tapıldı."
                        spambot = True
                    else:
                        ULIST = ["Bitmex", "Bitcoin", "Promotion","Information", "Dex","Announcements", "Info","Duyuru", "Duyurular","Bilgiləndirmə", "Bilgiləndirmələr"]
                        for i in ULIST:
                            if i in check_user.first_name:
                                if check_user.last_name == "Bot":
                                    reason = "Bilinen SpamBot"
                                    spambot = True

                    if spambot:
                        print(f"Bacarıq Spam Mesajı: {message.text}")
                        await message.delete()
                        break

                    continue  # Bir sonraki mesajı kontrol et

            if spambot:
                chat = await welcm.get_chat()
                admin = chat.admin_rights
                creator = chat.creator
                if not admin and not creator:
                    if ANTI_SPAMBOT_SHOUT:
                        await welcm.reply(
                            "@admin\n"
                            "`ANTI SPAMBOT Tapıldı!\n"
                            "BU User Mənim SpamBot Alqortimalarımıa Eşləşir!`"
                            f"SEBEP: {reason}")
                        kicked = False
                        reported = True
                else:
                    try:

                        await welcm.reply(
                            "`Bacarıq Spambot tapıldı !!`\n"
                            f"`SEBEP:` {reason}\n"
                            " İndi gruptan atılır, bu ID iləridəki durumlar üçün kaydediləcək.\n"
                            f"`KULLANICI:` [{check_user.first_name}](tg://user?id={check_user.id})"
                        )

                        await welcm.client.kick_participant(
                            welcm.chat_id, check_user.id)
                        kicked = True
                        reported = False

                    except BaseException:
                        if ANTI_SPAMBOT_SHOUT:
                            await welcm.reply(
                                "@admin\n"
                                "`Anti SpamBot Tapıldı!\n"
                                "Bu User Mənim SpamBot Alqoritmalarımla EşLəşir!`"
                                f"SEBEP: {reason}")
                            kicked = False
                            reported = True

                if BOTLOG:
                    if kicked or reported:
                        await welcm.client.send_message(
                            BOTLOG_CHATID, "#ANTI_SPAMBOT RAPORU\n"
                            f"Kullanıcı: [{check_user.first_name}](tg://user?id={check_user.id})\n"
                            f"Kullanıcı IDsi: `{check_user.id}`\n"
                            f"Sohbet: {welcm.chat.title}\n"
                            f"Sohbet IDsi: `{welcm.chat_id}`\n"
                            f"Sebep: {reason}\n"
                            f"Mesaj:\n\n{message.text}")
    except ValueError:
        pass


CMD_HELP.update({
    'anti_spambot':
    "Kullanım: Bu modul config.env dosyasında ya da env dəyəri ilə etkinləştirilmişsə,\
        \neğer bu spamcılar UserBot'un anti-spam alqoritmasıyla eşləşirsə, \
        \nbu modul qruptakı spamcıları gruptan qadağan edər (ya da adminlərə məlumat verir)."
})
