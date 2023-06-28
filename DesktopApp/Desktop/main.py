from flet import *
import flet
import conf
import sidebar
import init_sql



body = Container(
        Tabs(
            tabs=[
                sidebar.dashboard_button,
                sidebar.settings_button,
                sidebar.message_button,
            ],
        animation_duration=500,
        selected_index=1,
    ),
    width=conf.width,
    height=conf.height,
    bgcolor=conf.body_bg,
)

def manage(page:Page):
    page.window_max_width = conf.width
    page.window_max_height = conf.height
    page.window_width = conf.width
    page.window_height = conf.height
    page.padding = 0
    page.overlay.append(sidebar.message.file_picker)    
    page.add(
        body
    )

flet.app(manage,assets_dir="assets/")

