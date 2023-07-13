from flet import *
import flet
import conf
import sidebar
import init_sql
import login
import webapi
import threading

body = Container(
        Tabs(
            tabs=[
                sidebar.dashboard_button,
                sidebar.settings_button,
                sidebar.message_button,
                sidebar.categorys_button,
                sidebar.products_button,
            ],
        animation_duration=500,
        selected_index=4,
        indicator_color=conf.button_color,
        divider_color=conf.border_color,
    ),
    width=conf.width,
    height=conf.height,
    bgcolor=conf.background,
)

def manage(page:Page):
    page.window_min_width = conf.width
    page.window_min_height = conf.height
    page.window_max_width = conf.width
    page.window_max_height = conf.height
    page.window_width = conf.width
    page.window_height = conf.height
    page.padding = 0
    page.overlay.append(sidebar.message.file_picker)
    page.dialog = conf.alert        
    sidebar.categorys.Cancel()
    sidebar.products.load_data()
    page.add(
        body
    )
    webapi.api_info()

login.main_manage = manage


if len(init_sql.get_token())!=0:
    flet.app(manage,assets_dir="assets/")

else:
    flet.app(target=login.manage)
    if len(init_sql.get_token())!=0:
        flet.app(manage,assets_dir="assets/")