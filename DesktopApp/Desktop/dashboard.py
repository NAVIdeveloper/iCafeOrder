from flet import *
import flet
import conf

card_width = 320
card_height = 120
card_bg = "white"

dashboard = Container(
    Column([
        Row([
            Container(
                Row([
                    Image(src='assets/card_1.png'),
                    Column([
                        Text(
                            "89",
                            font_family=conf.font_family,
                            weight='w600',
                            color=conf.body_fg,
                            size=32,
                        ),
                        Text(
                            "Buyurtmalar soni",
                            font_family=conf.font_family,
                            weight='w400',
                            color=conf.body_fg,
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
                    Image(src='assets/card_2.png'),
                    Column([
                        Text(
                            "500,000",
                            font_family=conf.font_family,
                            weight='w600',
                            color=conf.body_fg,
                            size=32,
                        ),
                        Text(
                            "Tushgan Summa",
                            font_family=conf.font_family,
                            weight='w400',
                            color=conf.body_fg,
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
                    Image(src='assets/card_1.png'),
                    Column([
                        Text(
                            "102",
                            font_family=conf.font_family,
                            weight='w600',
                            color=conf.body_fg,
                            size=32,
                        ),
                        Text(
                            "Foydalanuvchilar soni",
                            font_family=conf.font_family,
                            weight='w400',
                            color=conf.body_fg,
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
                    Image(src='assets/card_2.png'),
                    Column([
                        Text(
                            "20",
                            font_family=conf.font_family,
                            weight='w600',
                            color=conf.body_fg,
                            size=32,
                        ),
                        Text(
                            "Mahsulotlar soni",
                            font_family=conf.font_family,
                            weight='w400',
                            color=conf.body_fg,
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
    ],spacing=50),
    width=conf.width,
    height=conf.height,
    bgcolor=conf.body_bg,
    padding=padding.only(100,50,100,50),
)