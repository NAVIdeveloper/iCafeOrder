import flet
from flet import *
import requests
import init_sql
import conf

WEB_API_URL = "http://127.0.0.1:8000/api/"


def login_check(e):
    user = username.value
    pas = password.value
    res=requests.post(WEB_API_URL+"login/",{"username":user,"password":pas})
    data = res.json()
    if data['status'] == True:
        token = data['token']
        init_sql.set_token(token)
        e.page.window_close()
        
        
        

main_manage = None

username = TextField(
    color=conf.font_color,
    height=60,
    hint_text="Username",
    hint_style=TextStyle(
        color=conf.light_font_color,
        weight='w400',
        size=18,
        font_family='consolas'
    ),
    text_style=TextStyle(
        size=18,
        font_family='consolas',
        weight='w400',
    ),
    # border_width=1,
    border_color=conf.icon_color,
    focused_border_width=1,
    border_radius=2,
)

password = TextField(
    color=conf.font_color,
    height=60,
    hint_text="Password",
    hint_style=TextStyle(
        color=conf.light_font_color,
        weight='w400',
        size=18,
        font_family='consolas'
    ),
    text_style=TextStyle(
        size=18,
        font_family='consolas',
        weight='w400',
    ),
    password=True,
    can_reveal_password=True,
    # border_width=1,
    border_color=conf.icon_color,
    focused_border_width=1,
    border_radius=2,
)

button = TextButton(
    "Kirish",                        
    style=ButtonStyle(
        color=conf.button_color,
        bgcolor=conf.font_color,
    ),
    width=500,
    height=40,
    on_click=login_check,
)

body = Container(
    Stack([
        Container(
            width=500,
            height=550,
            bgcolor=conf.background,
        ),
        Container(    
            Column([
                Container(
                    username,
                ),
                Container(
                    password,
                ),
                Container(
                    button,
                    padding=padding.all(50)
                )
            ],spacing=30),padding=padding.only(50,100,50),
        )
    ])
)

def manage(page:Page):
    page.window_width = 500
    page.window_height = 550
    page.window_resizable = False
    page.padding = 0
    # page.bgcolor = "#1c1c23"
    page.add(
        body
    )

# flet.app(target=manage)