# Mia UserBot - Ч ⁪⁬⁮⁮

""" UserBot başlangıç noktası """
import importlib
from importlib import import_module
from sqlite3 import connect
import os
import requests
import sys
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import GetMessagesRequest
from . import BRAIN_CHECKER, LOGS, bot, PLUGIN_CHANNEL_ID, CMD_HELP, LANGUAGE, BOSS_VERSION, PATTERNS, ForceVer
from .modules import ALL_MODULES
import userbot.modules.sql_helper.mesaj_sql as MSJ_SQL
import userbot.modules.sql_helper.galeri_sql as GALERI_SQL
from pySmartDL import SmartDL
from telethon.tl import functions

from random import choice
import chromedriver_autoinstaller
from json import loads, JSONDecodeError
import re
import userbot.cmdhelp

ALIVE_MSG = [
    "`Userbotunuz çalışıyor. Sana bişey demek istiyorum.. Seni seviyorum` **{mention}** ❤️",
    "🎆 `Endişelenme! Seni yanlız bırakmam.` **{mention}**, `MiaUserbot çalışıyor.`",
    "`⛈️ Elimden gelenin en iyisini yapmaya hazırım`, **{miasahip}**",
    "✨ `MiaUserBot sahibinin emirlerine hazır...`",
    "`Şuan en gelişmiş userbotun düzenlediği mesajı okuyor olmalısın` **{mention}**.",
    "`Benimi Aramıştın ❓ Ben Buradayım Merak Etme`"
    "`Userbotunuz çalışalı şu kadar oluyor:` **{worktime}** ❤️",
    "🎆 `Endişelenme! Seninleyim.` **{mention}**, `userbot çalışıyor.`",
    "`⛈️ Yeni gibi görünüyor!`, **{mention}:3**",
    "✨ `Userbot sahibinin emirlerine hazır...`",
    "`Huh!` **{mention}** `beni çağırıyor 🍰 < bu senin için 🥺..`",
    "{mention} **Mia Senin İçin Çalışıyor✨**",
    "{username}, `MiaUserBot {worktime} zamandır çalışıyor...`\n——————————————\n**Telethon sürümü :** `{telethon}`\n**Userbot sürümü  :** `{mia}`\n**Python sürümü    :** `{python}`\n**Plugin sayısı :** `{plugin}`\n——————————————\n**Emrine amadeyim dostum... 😇**"
]

DIZCILIK_STR = [
    "Stikeri əkirəm, palet eləməyin...",
    "Bunu oğurladım , geçmiş olsun 🤭",
    "Yaşasın əkmək...",
    "Bu stikeri öz paketimə dəvət edirəm ...",
]

AFKSTR = [
    "Şu an acele işim var, daha sonra mesaj atsan olmaz mı? Zaten yine geleceğim.",
    "Aradığınız kişi şu anda telefona cevap veremiyor. Sinyal sesinden sonra kendi tarifeniz üzerinden mesajınızı bırakabilirsiniz. Mesaj ücreti 49 kuruştur. \n`biiiiiiiiiiiiiiiiiiiiiiiiiiiiip`!",
    "Birkaç dakika içinde geleceğim. Fakat gelmezsem...\ndaha fazla bekle.",
    "Şu an burada değilim, ama muhtemelen başka bir yerdeyim.",
    "Güller kırmızı\nMenekşeler mavi\nBana bir mesaj bırak\nVe sana döneceğim.",
    "Bazen hayattaki en iyi şeyler beklemeye değer…\nHemen dönerim.",
    "Hemen dönerim,\nama eğer geri dönmezsem,\ndaha sonra dönerim.",
    "Henüz anlamadıysan,\nburada değilim.",
    "Merhaba, uzak mesajıma hoş geldiniz, bugün sizi nasıl görmezden gelebilirim?",
    "7 deniz ve 7 ülkeden uzaktayım,\n7 su ve 7 kıta,\n7 dağ ve 7 tepe,\n7 ovala ve 7 höyük,\n7 havuz ve 7 göl,\n7 bahar ve 7 çayır,\n7 şehir ve 7 mahalle,\n7 blok ve 7 ev...\n\nMesajların bile bana ulaşamayacağı bir yer!",
    "Şu anda klavyeden uzaktayım, ama ekranınızda yeterince yüksek sesle çığlık atarsanız, sizi duyabilirim.",
    "Şu yönde ilerliyorum\n---->",
    "Şu yönde ilerliyorum\n<----",
    "Lütfen mesaj bırakın ve beni zaten olduğumdan daha önemli hissettirin.",
    "Sahibim burada değil, bu yüzden bana yazmayı bırak.",
    "Burada olsaydım,\nSana nerede olduğumu söylerdim.\n\nAma ben değilim,\ngeri döndüğümde bana sor...",
    "Uzaklardayım!\nNe zaman dönerim bilmiyorum !\nUmarım birkaç dakika sonra!",
    "Sahibim şuan da müsait değil. Adınızı, numarınızı ve adresinizi verirseniz ona iletibilirm ve böylelikle geri döndüğü zaman.",
    "Üzgünüm, sahibim burada değil.\nO gelene kadar benimle konuşabilirsiniz.\nSahibim size sonra döner.",
    "Bahse girerim bir mesaj bekliyordun!",
    "Hayat çok kısa, yapacak çok şey var...\nOnlardan birini yapıyorum...",
    "Şu an burada değilim....\nama öyleysem ...\n\nbu harika olmaz mıydı?",
    "Beni hatırladığına sevindim ama şuanda klavye bana çok uzak",
    "Belki İyiyim, Belki Kötüyüm Bilmiyorsun Ama AFK Olduğumu Görebiliyorsun"
]

KICKME_MSG = [
    "Gülə-gülə mən gedirəm  👋🏻",
    "Yaxşı, tərk edirəm. 🥴",
    "Xəbərin olmadan çıxarsam , burada olmadığımın fərqinə vararsan.. Buna görə də bu mesajı buraxıram🚪",
    "cəld buradan çıxmalıyam.🤭",
    "7 dəniz və 7 ölkə,\n7 su və 7 qitə,\n7 dağ və 7 təpə,\n7 ovala və 7 höyük,\n7 hovuz ve 7 göl,\n7 bahar və 7 çayır,\n7 şəhər və 7 məhəllə,\n7 blok və 7 ev...\n\nQısaca bu qrupdan uzaq bir yerə.!",
    "Davay mən getdim!"
]


UNAPPROVED_MSG = ("`{mention} Sahibim təsdiq edənə qədər bu mesajı alacaqsan👩🏻‍💻!\n\n`"
                  "`✔️ Təsdiq olunmadığın müddətdə sahibim əvəzinə mən yazacağam  `")

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()


INVALID_PH = '\nXəta: Girilən telefon nömrəsi geçərsiz' \
             '\n  Ipucu: Ölkə kodunu yazmağı unutma ' \
             '\n   Telefon nömrəni yenidən yoxla'

for i in ALL_ROWS:
    BRAIN_CHECKER.append(i[0])
connect("learning-data-root.check").close()
BRAIN_CHECKER = BRAIN_CHECKER[0]

def extractCommands(file):
    FileRead = open(file, 'r').read()
    
    if '/' in file:
        file = file.split('/')[-1]

    Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", FileRead)
    Komutlar = []

    if re.search(r'CmdHelp\(.*\)', FileRead):
        pass
    else:
        dosyaAdi = file.replace('.py', '')
        CmdHelp = userbot.cmdhelp.CmdHelp(dosyaAdi, False)

        # Komutları Alıyoruz #
        for Command in Pattern:
            Command = Command[1]
            if Command == '' or len(Command) <= 1:
                continue
            Komut = re.findall("(^.*[a-zA-Z0-9şğüöçı]\w)", Command)
            if (len(Komut) >= 1) and (not Komut[0] == ''):
                Komut = Komut[0]
                if Komut[0] == '^':
                    KomutStr = Komut[1:]
                    if KomutStr[0] == '.':
                        KomutStr = KomutStr[1:]
                    Komutlar.append(KomutStr)
                else:
                    if Command[0] == '^':
                        KomutStr = Command[1:]
                        if KomutStr[0] == '.':
                            KomutStr = KomutStr[1:]
                        else:
                            KomutStr = Command
                        Komutlar.append(KomutStr)

            # MIAPY
            Bosspy = re.search('\"\"\"BOSSPY(.*)\"\"\"', FileRead, re.DOTALL)
            if not Bosspy == None:
                Bosspy = Siripy.group(0)
                for Satir in Bosspy.splitlines():
                    if (not '"""' in Satir) and (':' in Satir):
                        Satir = Satir.split(':')
                        Isim = Satir[0]
                        Deger = Satir[1][1:]
                                
                        if Isim == 'INFO':
                            CmdHelp.add_info(Deger)
                        elif Isim == 'WARN':
                            CmdHelp.add_warning(Deger)
                        else:
                            CmdHelp.set_file_info(Isim, Deger)
            for Komut in Komutlar:
                # if re.search('\[(\w*)\]', Komut):
                    # Komut = re.sub('(?<=\[.)[A-Za-z0-9_]*\]', '', Komut).replace('[', '')
                CmdHelp.add_command(Komut, None, 'Bu plugin kənardan yükləmib. Hansısa bir açıqlama qeyd etməyiblər .')
            CmdHelp.add()

forceVer = []
DB = connect("force-surum.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM SURUM1""")
ALL_ROWS = CURSOR.fetchall()

for i in ALL_ROWS:
    forceVer = i
connect("force-surum.check").close() 

try:
    ForceVer = int(forceVer)
except:
    ForceVer = -1


try:
    bot.start()
    idim = bot.get_me().id
    bossbl = requests.get('https://raw.githubusercontent.com/bossuserb/datas/master/blacklist.json').json()
    if idim in bossbl:
        bot.send_message("me", f"`❌ Boss inzibatçıları səni botdan qadağan etdi! Bot söndürülür...`")
        LOGS.error("Mia yöneticileri sizi bottan yasakladı! Bot kapatılıyor...")
        bot.disconnect()
        sys.exit(1)
    # ChromeDriver'ı Ayarlayalım #
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    
    # Galeri için değerler
    GALERI = {}

    # PLUGIN MESAJLARI AYARLIYORUZ
    PLUGIN_MESAJLAR = {}
    ORJ_PLUGIN_MESAJLAR = {"alive": f"{str(choice(ALIVE_MSG))}", "afk": f"`{str(choice(AFKSTR))}`", "kickme": f"`{str(choice(KICKME_MSG))}`", "pm": str(UNAPPROVED_MSG), "dızcı": str(choice(DIZCILIK_STR)), "ban": "🌀 {mention}`, Banlandı!!`", "mute": "🌀 {mention}`, səssizə alındı!`", "approve": "`Salam` {mention}`, daha mənə mesaj göndərə bilərsən!`", "disapprove": "{mention}`, artıq mənə mesaj göndərə bilmərsən!`", "block": "{mention}`, buna məni məcbur etdin! Səni əngəllədim!`"}


    PLUGIN_MESAJLAR_TURLER = ["alive", "afk", "kickme", "pm", "dızcı", "ban", "mute", "approve", "disapprove", "block"]
    for mesaj in PLUGIN_MESAJLAR_TURLER:
        dmsj = MSJ_SQL.getir_mesaj(mesaj)
        if dmsj == False:
            PLUGIN_MESAJLAR[mesaj] = ORJ_PLUGIN_MESAJLAR[mesaj]
        else:
            if dmsj.startswith("MEDYA_"):
                medya = int(dmsj.split("MEDYA_")[1])
                medya = bot.get_messages(PLUGIN_CHANNEL_ID, ids=medya)

                PLUGIN_MESAJLAR[mesaj] = medya
            else:
                PLUGIN_MESAJLAR[mesaj] = dmsj
    if not PLUGIN_CHANNEL_ID == None:
        LOGS.info("🔄 Pluginlər Yüklənir..")
        try:
            KanalId = bot.get_entity(PLUGIN_CHANNEL_ID)
        except:
            KanalId = "me"

        for plugin in bot.iter_messages(KanalId, filter=InputMessagesFilterDocument):
            if plugin.file.name and (len(plugin.file.name.split('.')) > 1) \
                and plugin.file.name.split('.')[-1] == 'py':
                Split = plugin.file.name.split('.')

                if not os.path.exists("./userbot/modules/" + plugin.file.name):
                    dosya = bot.download_media(plugin, "./userbot/modules/")
                else:
                    LOGS.info("Bu Plugin Onsuzda Yüklüdür " + plugin.file.name)
                    extractCommands('./userbot/modules/' + plugin.file.name)
                    dosya = plugin.file.name
                    continue 
                
                try:
                    spec = importlib.util.spec_from_file_location("userbot.modules." + Split[0], dosya)
                    mod = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(mod)
                except Exception as e:
                    LOGS.info(f"`[×] Yükləmək uğursuz! Plugin xətalıı!!\n\nXəta: {e}`")

                    try:
                        plugin.delete()
                    except:
                        pass

                    if os.path.exists("./userbot/modules/" + plugin.file.name):
                        os.remove("./userbot/modules/" + plugin.file.name)
                    continue
                extractCommands('./userbot/modules/' + plugin.file.name)
    else:
        bot.send_message("me", f"`Pluginlərin heç vaxt silinməməsi üçün zəhmət olmazsa  PLUGIN_CHANNEL_ID qeyd edin.`")
except PhoneNumberInvalidError:
    print(INVALID_PH)
    sys.exit(1)

async def FotoDegistir (foto):
    FOTOURL = GALERI_SQL.TUM_GALERI[foto].foto
    r = requests.get(FOTOURL)

    with open(str(foto) + ".jpg", 'wb') as f:
        f.write(r.content)    
    file = await bot.upload_file(str(foto) + ".jpg")
    try:
        await bot(functions.photos.UploadProfilePhotoRequest(
            file
        ))
        return True
    except:
        return False

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

os.system("clear")

LOGS.info("+===========================================================+")
LOGS.info("|                     ✨Boss Userbot✨                       |")
LOGS.info("+==============+==============+==============+==============+")
LOGS.info("|                                                            |")
LOGS.info("Botunuz işləyir! Hansısa bir söhbətə .alive yazaraq Test edin."
          " Köməyə ehtiyacınız varsa, Dəstəkk qrupumuza gəlin t.me/bosssupportaz")
LOGS.info(f"Bot versiyonunuz: Boss {BOSS_VERSION}")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
