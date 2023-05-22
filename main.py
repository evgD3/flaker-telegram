from aiogram import Bot, Dispatcher, executor, types
from faker import Faker

from config import TELEGRAM_TOKEN


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    fake = Faker("ru_RU")
    name = fake.name()
    address = fake.address()
    phone_number = fake.phone_number()
    job = fake.job()
    mail = fake.ascii_free_email()
    site = fake.hostname()
    company = fake.company()
    await message.answer(f'ФИO: {name}'
                         f'\nадрес: {address}'
                         f'\nтелефон: {phone_number}'
                         f'\nпочта: {mail}'
                         f'\nпрофессия: {job}'
                         f'\nсайт: {site}'
                         f'\nкомпания: {company}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
