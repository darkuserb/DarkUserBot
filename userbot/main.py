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
    "`Userbotunuz işləyir. Sənə bir şey demək istəyirəm. Səni sevirəm` **{mention}** ❤️",
    "🎆 `Narahat olma! Səni tək buraxmaram.` **{mention}**, `BossUserbot işləyir.`",
    "`⛈️ Əlimdən gələnin ən yaxşısını etməyə çalışıram`, {mention}",
    "✨ `bossuserbot sahibinin əmrlərinə hazır...`",
    "`Hal-hazırda ən yaxşı userbotun hazırlandığı mesajı oxuyur olmalısan` **{mention}**.",
    "`Boss'u axtarırdın ❓  Mən burdayam, kef elə`"
    "`Userbotunuz işləyəli bu qədər olur:` **{worktime}** ❤️",
    "🎆 `Narahat olma! Səninləyəm.` **{mention}**, `userbot işləyir.`",
    "`⛈️ Yeni kimi görünür!`, **{mention}<3**",
    "✨ `Userbot sahibinin əmrinə hazır...`",
    "`Huh!` **{mention}** `məni çağırır 🍰 < bu sənin üçündü 🥺..`",
    "{mention} **Boss  sənin üçün işləyir✨**",
    "{username}, `bossuserbot {worktime} zamandır işləyir...`\n——————————————\n**Telethon sürümü :** `{telethon}`\n**Userbot sürümü  :** `{boss}`\n**Python sürümü    :** `{python}`\n**Plugin sayı :** `{plugin}`\n——————————————\n**Əmrinə tabeyəm dostum... 😇**"
]

DIZCILIK_STR = [
    "Stikeri əkirəm, palet eləməyin...",
    "Bunu oğurladım , geçmiş olsun 🤭",
    "Yaşasın əkmək...",
    "Bu stikeri öz paketimə dəvət edirəm ...",
]

AFKSTR = [
    "İndi tələsirəm işim var, daha sonra mesaj atsan olmaz dı? Onsuz yenə gələcəm.",
    "Çağırdığınız kişi indi telefona cavab verə bilmir. Siqnal səsindən sonra öz tərifiniz üzərindən mesajınızı buraxa bilərsiniz. Mesaj haqqı 49 qəpikdir. \n`biiiiiiiiiiiiiiiiiiiiiiiiiiiiip`!",
    "Bir neçə dəqiqəyə gələcəm. gəlməzsəm...\ndaha çox gözlə.",
    "İndi burada deyiləm, ama ehtimal edirəmki başqa bir yerdəyəm.",
    "Güllər qırmızı\bənövşələr mavi\nMənə bir mesaj buraz\nVə sənə dönəcəm.",
    "Bəzən həyattakı ən yaxşı şeyləri gözləməyə dəyər…\nİndi dönürəm.",
    "İndi gəlirəm,\namma əgər geri gəlməzsəm,\ndaha sonra gələrəm.",
    "İndi anlamamısansa,\nburada deyiləm.",
    "Salam, uzaq mesajıma xoş gəldiniz, bugün sizi necə görməzdən gələ bilərəm?",
    "7 dəniz və 7 ölkədən uzaqdayam,\n7 su və 7 qitə,\n7 dağ və 7 təpə,\n7 ovala və 7 kurqan,\n7 hovuz və 7 göl,\n7 yaz və 7 çəmən,\n7 şəhər və 7 məhəllə,\n7 blok və 7 ev...\n\nMesajların belə mənə çata bilməyəcəyi bir yer!",
    "Bu dəqiqə klaviyaturadan uzaqdayaç, amma ekranınızda yetərincə yüksek səslə qışqırsanəz, sizi eşidə bilərəm.",
    "Bu yöndə gedirəm\n---->",
    "Bu yöndə qaçıram\n<----",
    "Xahiş mesaj buraxın və məni olduğumdan daha özəl hiss etdirin.",
    "Sahibim burada deyil, bu səbəbdən mənə yazma.",
    "Burada olsaydım,\nSənə harada olduğumu deyərdim.\n\nAmma mən deyiləm,\ngeri gəldiyimdə mənə de...",
    "Uzaqlardayam!\nNə zaman gələrəm bilmirəm !\nÜmid varamki bir neçə dəqiqə sonra!",
    "Sahibim indi məşğuldur. Adınızı, nömrənizi və adresinizi versəniz ona ata bilərəm və beləlikle geri döndüyü zaman.",
    "Təəssüf ki, sahibim burada deyil.\nO gələnə qədər mənlə danışa bilərsiniz.\nSahibim sizə sonra baxar.",
    "Bəhsə girərəm bir mesaj gözləyirdin!",
    "Həyat çox qısa, edəcək çox şey var...\nOnlardan birini edirəm...",
    "İndi burada deyiləm....\namma eləsəmm ...\n\nbu yaxşı olmaz mıydı?",
    "Məni xatırladığına sevindim ama indi klaviyatura mənə çox uzaq",
    "Bəlkə yaxşıyam, Bəlkə pis Bilmirsən Ama AFK Olduğumu Görə bilirsən"
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
                CmdHelp.add_command(Komut, None, 'Bu plugin kənardan yüklənib. Hansısa bir açıqlama qeyd etməyiblər .')
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
        LOGS.error("Boss inzibatçıları səni botdan qadağan etdi! Bot söndürülür...")
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
