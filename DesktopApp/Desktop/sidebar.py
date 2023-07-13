from flet import *
import flet
import conf
import dashboard
import settings
import message
import categorys
import products

WIDTH = 200
HEIGHT = conf.height
BG = "white"
BTN_HEIGHT = 50
        

dashboard_button = Tab(
    tab_content=Text(
        "Dashboard",
        color=conf.font_color,
        font_family=conf.font_family,
    ),
    content=dashboard.dashboard,
)

settings_button = Tab(
    tab_content=Text(
        "Sozlamalar",
        color=conf.font_color,
        font_family=conf.font_family,
    ),
    content=settings.settings,
)

message_button = Tab(
    tab_content=Text(
        "Xabar Yuborish",
        color=conf.font_color,
        font_family=conf.font_family,
    ),
    content=message.message,
)
categorys_button = Tab(
    tab_content=Text(
        "Kategoriyalar",
        color=conf.font_color,
        font_family=conf.font_family,
    ),
    content=categorys.categorys,
)

products_button = Tab(
    tab_content=Text(
        "Mahsulotlar",
        color=conf.font_color,
        font_family=conf.font_family,
    ),
    content=products.products,
)
