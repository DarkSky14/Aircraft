from pygame import font, init
try:
    from logged import log

    from language import LanguageCreater, LanguageSetter
    from FileWorker import JsonReader, JsonWorker

    from Surface import AdjustmentSubSurface, AdjustmentSurface, ScrollingBG
    from event import EventControl

    from Text import Text, ModuleText
    from UI import Button, ModuleButton, SurfaceM

except:
    from clients.module.logged import log

    from clients.module.language import LanguageCreater, LanguageSetter
    from clients.module.FileWorker import JsonReader, JsonWorker

    from clients.module.Surface import AdjustmentSubSurface, AdjustmentSurface
    from clients.module.event import EventControl

    from clients.module.Text import Text, ModuleText
    from clients.module.UI import Button, ModuleButton, SurfaceM

init()


main_surface = AdjustmentSurface().surface() # 960, 544 StandartSurface(960, 544) #
GLOBAL_EVENT = AdjustmentSubSurface(1373, 761)# Original size 300x168
d = GLOBAL_EVENT.surface(main_surface)
main_surface.fill((0, 0, 0))
d.fill((255, 255, 255))

screen = GLOBAL_EVENT.get_size_surface()
conf_width = GLOBAL_EVENT.get_conf_width()
conf_height = GLOBAL_EVENT.get_conf_height()
procent = GLOBAL_EVENT.get_procent()
height = d.get_height()
width =  d.get_width()

log.debug({"Main surface size": screen})


config = JsonWorker(
    "config",
    "library/data",
    {
        "level": 1, 
        "effect": "True", 
        "music": "True", 
        "language": "EN"
    },
    "config.json"
)
config.reader()

temp = JsonWorker(
    "temp",
    "none",
    {"musicID": "None"}
)
log.debug({"INITIALIAZE_TEMP": temp.get_data()})


GLOBAL_EVENT = EventControl(200, conf_width, conf_height)


ENG = LanguageCreater("EN", "library/language", "english.json")
ENG.set_lang(JsonReader)
ENGLISH = ENG.get_lang()

UKR = LanguageCreater("UA", "library/language", "ukrainian.json")
UKR.set_lang(JsonReader)
UKRAINIAN = UKR.get_lang()

language = LanguageSetter(config).language_set(ENG, UKR)
log.info("LANGUAGE LOADED...")


VERS_GAME = font.SysFont(None, round(20 * procent))

text = Text(VERS_GAME, language, d, config, (0,0,0))
big_text = ModuleText(text.copy())
#big_text = text.copy()
big_text.create_font('Georgia', round(36 * procent))

standart_text = ModuleText(text.copy())
standart_text.create_font('Georgia', round(21 * procent))