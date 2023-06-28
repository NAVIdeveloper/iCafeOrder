from flet import *
import flet
import conf
import init_sql

bg = 'white'
border_color = 'green'

def Save_Field(e):
    start = field_start.value
    order = field_order.value
    run = field_run.value
    about = field_about.value
    init_sql.update_data(start,order,run,about)
    print(init_sql.get_data())
    # print(start)
    # print(order)
    # print(run)
    # print(about)

data = init_sql.get_data()

field_start = TextField(
    value=data['start'],
    border=InputBorder.UNDERLINE,
    border_color=border_color,
    filled=True,
    hint_text="Kirish matni..",
    multiline=True,
    min_lines=2,
)

field_order = TextField(
    value=data['text_order'],
    border=InputBorder.UNDERLINE,
    border_color=border_color,
    filled=True,
    hint_text="Buyurtma olingadagi matn..",
    multiline=True,
    min_lines=2,
)

field_run = TextField(
    value=data['run'],
    border=InputBorder.UNDERLINE,
    border_color=border_color,
    filled=True,
    hint_text="Bot ishga tushganidagi matn..",
    multiline=True,
    min_lines=2,
)

field_about = TextField(
    value=data['about'],
    border=InputBorder.UNDERLINE,
    border_color=border_color,
    filled=True,
    hint_text="Bot haqida matni..",
    multiline=True,
    min_lines=2,
)

submit_btn = flet.ElevatedButton(
    "Saqlash",
    width=150,
    icon=icons.DONE,
    on_click=Save_Field,
)

settings = Container(
    Column([
        field_start,
        field_order,
        field_run,
        field_about,
        Container(
            submit_btn,
        )
    ],scroll='auto'),
    margin=margin.only(50,50,50,100),
    padding=padding.all(15),
    bgcolor=bg,
    border_radius=3,
)