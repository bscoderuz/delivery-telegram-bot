from aiogram.types import Message
from keyboards.inline.productsKeyboard import categoryMenu
from loader import dp


@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(message: Message):
    await message.answer(f"Kategoriyalardan birini tanlang", reply_markup=categoryMenu)
