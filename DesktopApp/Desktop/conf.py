from flet import *

width = 920
height = 700
background = "white"
font_color = "#1B2021"
light_font_color="#951B2021"
card_bg = "#f1f3f4"
icon_color = "#9649CB"

button_color = "#49A078"

border_color= button_color#'#CCCCCC'

font_family = "IBM Plex Sans"

font_weight = 400

BOT_TOKEN = ""
WEB_API_URL = "http://127.0.0.1:8000/api/"

file_picker = FilePicker()
alert = AlertDialog(
        modal=True,
        title=Text("Yangi",weight='w500',color=font_color),
        content=Container(
            Column([]),
            alignment=alignment.center,
            padding=padding.only(bottom=20),
            width=300,
        ),
    )