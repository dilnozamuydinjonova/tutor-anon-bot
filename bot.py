import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [x.strip() for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Assalomu alaykum!\n\n"
        "Bu anonim tutorga murojaat boti.\n"
        "Murojaatingizni shu chatga yozib qoldiring."
    )

@dp.message()
async def forward_to_admins(message: Message):
    text = message.text or "(matn emas)"
    for admin_id in ADMIN_IDS:
        if admin_id.isdigit():
            await bot.send_message(int(admin_id), f"📩 Yangi murojaat:\n\n{text}")
    await message.answer("✅ Murojaatingiz yuborildi. Rahmat!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
