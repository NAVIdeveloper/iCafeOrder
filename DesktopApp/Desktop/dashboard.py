from flet import *
import flet
import conf

card_width = 320
card_height = 120
card_bg = conf.card_bg

count_order = Text(
    "89",
    font_family=conf.font_family,
    weight='w600',
    color=conf.font_color,
    size=32,
)
total_sum = Text(
    "500,000",
    font_family=conf.font_family,
    weight='w600',
    color=conf.font_color,
    size=32,
)
count_user = Text(
    "102",
    font_family=conf.font_family,
    weight='w600',
    color=conf.font_color,
    size=32,
)
count_product = Text(
    "20",
    font_family=conf.font_family,
    weight='w600',
    color=conf.font_color,
    size=32,
)

def OnOfChange(e):
    import BOT
    if e.control.value == True:
        BOT.bot.polling()
        e.control.label = "Bot ishlamoqda."
        
    else:
        BOT.bot.stop_polling()
        e.control.label = "Bot o'chirilgan."
    e.control.update()

dashboard = Container(
    Column([
        Row([
            Container(
                Row([
                    Column([
                        count_order,
                        Text(
                            "Buyurtmalar soni",
                            font_family=conf.font_family,
                            weight='w400',
                            color=conf.font_color,
                            size=20,
                        )
                    ],spacing=0)
                ]),
                width=card_width,
                height=card_height,
                padding=20,
                bgcolor=card_bg,
                border_radius=3,
            ),
            Container(
                Row([
                    Column([
                        total_sum,
                        Text(
                            "Tushgan Summa",
                            font_family=conf.font_family,
                            weight='w400',
                            color=conf.font_color,
                            size=20,
                        )
                    ],spacing=0)
                ]),
                width=card_width,
                height=card_height,
                padding=20,
                bgcolor=card_bg,
                border_radius=3,
            ),
        ],alignment='spaceBetween'),
        Row([
            Container(
                Row([
                    Column([
                        count_user,
                        Text(
                            "Foydalanuvchilar soni",
                            font_family=conf.font_family,
                            weight='w400',
                            color=conf.font_color,
                            size=20,
                        )
                    ],spacing=0)
                ]),
                width=card_width,
                height=card_height,
                padding=20,
                bgcolor=card_bg,
                border_radius=3,
            ),
            Container(
                Row([
                    Column([
                        count_product,
                        Text(
                            "Mahsulotlar soni",
                            font_family=conf.font_family,
                            weight='w400',
                            color=conf.font_color,
                            size=20,
                        )
                    ],spacing=0)
                ]),
                width=card_width,
                height=card_height,
                padding=20,
                bgcolor=card_bg,
                border_radius=3,
            ),
        ],alignment='spaceBetween'),
        Container(
            Switch(
                label="Bot o'chirilgan.",
                value=False,
                active_color='white',
                active_track_color=conf.button_color,
                on_change=OnOfChange,
            ),
        )
    ],spacing=50),
    width=conf.width,
    height=conf.height,
    bgcolor=conf.background,
    padding=padding.only(100,50,100,50),
)