import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils import executor
from rembg import remove
from io import BytesIO
from PIL import Image

API_TOKEN = "7026349704:AAEaXwMeS-FS2cUf2PEe1CaYOrp5IXGRCx0"


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Rasm tashlang uni bgsini olib taashlayman")


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message: types.Message):

    photo = message.photo[-1]
    photo_file = await bot.download_file_by_id(photo.file_id)


    input_image = Image.open(photo_file)
    output_image = remove(input_image)


    output_buffer = BytesIO()
    output_image.save(output_buffer, format='PNG')
    output_buffer.seek(0)


    await bot.send_photo(message.chat.id, photo=InputFile(output_buffer, filename='output.png'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
