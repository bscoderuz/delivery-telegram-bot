from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mahsulotlar"),
            KeyboardButton(text="Qo'llanma",)
        ],
        [
            KeyboardButton(text="⚙Sozlamalar")
        ]
    ],
    resize_keyboard=True
)
