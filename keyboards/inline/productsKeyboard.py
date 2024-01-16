from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import product_callback

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒Buyurtma berish", callback_data="product"),
        ],
        [
            InlineKeyboardButton(text="ℹ️Biz haqimizda", callback_data='data'),
            InlineKeyboardButton(text="🛍Buyurtmalarim", callback_data='data'),
        ],
        [
            InlineKeyboardButton(text="🏬Filiallar", callback_data="filiallar"),
        ],
        [
            InlineKeyboardButton(text="✍🏻Firkr bildirish", callback_data="data"),
            InlineKeyboardButton(text="⚙️Sozlamalar", callback_data='settings'),
        ],
    ])
