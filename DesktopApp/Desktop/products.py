from flet import *
import flet
from webapi import *
import conf

def EditProduct(e):
    print(e.control.data)
    e.page.overlay.append(conf.file_picker)
    e.control.update()
    data=None
    for i in api_products_get():
        if i['id'] == e.control.data:
            data = i
            break

    def on_res(e):
        if len(e.files) > 0:
            src=e.files[0].path
            image.src=src
            img = src
            e.page.update()
    conf.file_picker.on_result = on_res
    def close(ee):
        ee.page.dialog.open = False
        load_data()
        ee.page.update()

    def del_ask(e):
        def delete(e):
            api_products_delete(data['id'])
            close(e)

        e.page.dialog.actions = [
            ElevatedButton(
                "O'chirish",
                icon=icons.DELETE,
                icon_color='red',
                color='red',
                on_click=delete,
                data=data['id'],
            ),
            ElevatedButton(
                "Bekor qilish",
                icon=icons.CANCEL,
                icon_color=conf.button_color,
                color=conf.button_color,
                on_click=close,
            )
        ]
        e.page.dialog.update()
        
    
    def save(e):
        img = None
        if not image.src == data['image']:
            img = image.src
        api_products_edit(
            id=e.control.data,
            name=new_name.value,
            category=new_category.value,
            price=new_price.value,
            image=img,
            about=new_about.value,
        )
        close(e)

    image = Image(src=data['image'],width=150,height=150)
    img = None
    new_image = ElevatedButton(
        "Rasm tanlash",
        icon=icons.FILE_OPEN,
        color=conf.button_color,
        icon_color=conf.button_color,
        on_click=lambda e:conf.file_picker.pick_files("Rasm",allow_multiple=False),
    )
    new_name = TextField(
        hint_text="Nomi...",
        color=conf.font_color,
        text_size=16,
        value=data['name'],
        border=InputBorder.UNDERLINE,
        border_color=conf.button_color,
    )
    category = api_categorys_get()
    categorys = []
    for i in category[::-1]:
        categorys.append(
            dropdown.Option(
                key=i['id'],
                text=i['name'],
            )
        )
    new_category = Dropdown(
        options=categorys,
        height=40,
        border='underline',
        border_color=conf.font_color,
        label=data['category']['name'],
        value=data['category']['id'],
    )
    new_price = TextField(
        hint_text="Narxi...",
        color=conf.font_color,
        text_size=16,
        border=InputBorder.UNDERLINE,
        border_color=conf.button_color,
        value=data['price']
    )
    new_about = TextField(
        hint_text="Qo'shimcha...",
        color=conf.font_color,
        text_size=16,
        multiline=True,
        max_lines=2,
        border=InputBorder.UNDERLINE,
        border_color=conf.button_color,
        value=data['about']
    )
    e.page.dialog.content=Container(
        Column([
            image,
            new_image,
            new_name,
            new_category,
            new_price,
            new_about
        ]),
        alignment=alignment.center,
        padding=padding.only(bottom=20),
        width=300,
    )
    e.page.dialog.title=Text("Tahrirlash",weight='w500',color=conf.font_color)
    
    e.page.dialog.actions=[
        ElevatedButton(
            "Saqlash",
            icon=icons.CHECK,
            icon_color=conf.button_color,
            color=conf.button_color,
            on_click=save,
            data=data['id'],
        ),
        ElevatedButton(
            "Yopish",
            icon=icons.CANCEL,
            icon_color=conf.button_color,
            color=conf.button_color,
            on_click=close,
        ),
        ElevatedButton(
            "O'chirish",
            icon=icons.DELETE,
            icon_color='orange',
            color='orange',
            on_click=del_ask,
        ),
        
    ]

    e.page.dialog.open = True
    e.page.update()

def AddNew(e):
    e.page.overlay.append(conf.file_picker)
    e.control.update()
    
    def on_res(e):
        if len(e.files) > 0:
            src=e.files[0].path
            image.src=src
            e.page.update()
    conf.file_picker.on_result = on_res
    def close(ee):
        ee.page.dialog.open = False
        load_data()
        ee.page.update()
        
    
    def add(e):
        api_products_add(
            name=new_name.value,
            category=new_category.value,
            price=new_price.value,
            image=image.src,
            about=new_about.value,
        )
        close(e)

    image = Image(src='None',width=150,height=150)
    new_image = ElevatedButton(
        "Rasm tanlash",
        icon=icons.FILE_OPEN,
        color=conf.button_color,
        icon_color=conf.button_color,
        on_click=lambda e:conf.file_picker.pick_files("Rasm",allow_multiple=False),
    )
    new_name = TextField(
        hint_text="Nomi...",
        color=conf.font_color,
        text_size=16,
        border=InputBorder.UNDERLINE,
        border_color=conf.button_color,
    )
    category = api_categorys_get()
    categorys = []
    for i in category[::-1]:
        categorys.append(
            dropdown.Option(
                key=i['id'],
                text=i['name'],
            )
        )
    new_category = Dropdown(
        options=categorys,
        height=40,
        border='underline',
        border_color=conf.font_color,
    )
    new_price = TextField(
        hint_text="Narxi...",
        color=conf.font_color,
        text_size=16,
        border=InputBorder.UNDERLINE,
        border_color=conf.button_color,
    )
    new_about = TextField(
        hint_text="Qo'shimcha...",
        color=conf.font_color,
        text_size=16,
        multiline=True,
        max_lines=2,
        border=InputBorder.UNDERLINE,
        border_color=conf.button_color,
    )
    e.page.dialog.title=Text("Yangi",weight='w500',color=conf.font_color)
    e.page.dialog.content=Container(
        Column([
            image,
            new_image,
            new_name,
            new_category,
            new_price,
            new_about
        ]),
        alignment=alignment.center,
        padding=padding.only(bottom=20),
        width=300,
    )
    e.page.dialog.actions=[
        ElevatedButton(
            "Tasdiqlash",
            icon=icons.ADD,
            icon_color=conf.button_color,
            color=conf.button_color,
            on_click=add,
        ),
        ElevatedButton(
            "Yopish",
            icon=icons.CANCEL,
            icon_color=conf.button_color,
            color=conf.button_color,
            on_click=close,
        ),
    ]
    
    e.page.dialog.open = True
    e.page.update()
    

rows = [
    
]
items = Row(
    rows,
    wrap=True,
)
def load_data():
    global rows
    try:
        rows = []
        data = api_products_get()
        for i in data[::-1]:
            rows.append(
                Container(
                    Column([
                        Image(src=i['image'],border_radius=8),
                        Row([
                            Text(
                                "Nomi:",
                                color=conf.light_font_color,
                                size=16,
                                weight='w400'
                            ),
                            Text(
                                i['name'],
                                color=conf.font_color,
                                size=16,
                                weight='w400'
                            ),
                        ]),
                        Row([
                            Text(
                                "Categorya:",
                                color=conf.light_font_color,
                                size=16,
                                weight='w400'
                            ),
                            Text(
                                i['category']['name'],
                                color=conf.font_color,
                                size=16,
                                weight='w400'
                            ),
                        ]),
                        Row([
                            Text(
                                "Narxi:",
                                color=conf.light_font_color,
                                size=16,
                                weight='w400'
                            ),
                            Text(
                                "{:,}".format(i['price']),
                                color=conf.font_color,
                                size=16,
                                weight='w400'
                            ),
                        ]),
                        Row([
                            IconButton(
                                icons.EDIT,
                                icon_color=conf.button_color,
                                data=i['id'],
                                on_click=EditProduct,
                            ),
                            Text(
                                "Tahrirlash",
                                color='#1d1e2c',
                                size=16,
                                weight='w400'
                            )
                        ])
                    ]),
                    width=250,
                    # bgcolor='white',
                    border_radius=8,
                    border=border.all(1,conf.border_color),
                    padding=padding.all(20),
                )
            )
        items.controls=rows
    except:
        pass
load_data()

products = Container(
    Column([
        Container(
            ElevatedButton(
                "Yangi qo'shish",
                icon=icons.ADD,
                color=conf.button_color,
                icon_color=conf.button_color,
                on_click=AddNew,
            )
        ),
        items,
        
    ],scroll='always'),
    width=conf.width,
    padding=padding.only(50,30,50,50),
)