from flet import *
import flet
import conf
import dashboard
import settings
import message

WIDTH = 200
HEIGHT = conf.height
BG = "white"
BTN_HEIGHT = 50
        

dashboard_button = Tab(
    tab_content=Text(
        "Dashboard",
        color=conf.body_fg,
        font_family=conf.font_family,
    ),
    content=dashboard.dashboard,
)

settings_button = Tab(
    tab_content=Text(
        "Sozlamalar",
        color=conf.body_fg,
        font_family=conf.font_family,
    ),
    content=settings.settings,
)

message_button = Tab(
    tab_content=Text(
        "Xabar Yuborish",
        color=conf.body_fg,
        font_family=conf.font_family,
    ),
    content=message.message,
)
