from flet import *
import flet
import conf

bg = 'white'
border_color = 'green'
file_picker = FilePicker()

field_message = TextField(
    border=InputBorder.UNDERLINE,
    border_color=border_color,
    filled=True,
    hint_text="Xabar",
    multiline=True,
    min_lines=3,
)

message_btn=ElevatedButton(
    "xabarni barchaga yuborish",
    icon=icons.SEND,
    #on_click need
)

message = Container(
    Column([
        # ElevatedButton(
        #     "Rasm Tanlash...",
        #     on_click=lambda _: file_picker.pick_files()
        # ),
        field_message,
        message_btn,
    ],scroll='auto'),
    margin=margin.only(50,50,50,100),
    padding=padding.all(15),
    bgcolor=bg,
    border_radius=3,
)