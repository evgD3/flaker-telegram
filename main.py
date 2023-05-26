import telebot
from faker import Faker

from config import TELEGRAM_TOKEN


bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'start/help')

@bot.message_handler(commands=['gen'])
def gen_persone(message):
    fake = Faker("ru_RU")
    name = fake.name()
    address = fake.address()
    phone_number = fake.phone_number()
    job = fake.job()
    mail = fake.ascii_free_email()
    site = fake.hostname()
    company = fake.company()
    bot.reply_to(message,
                   f'ФИO: {name}'
                   f'\nадрес: {address}'
                   f'\nтелефон: {phone_number}'
                   f'\nпочта: {mail}'
                   f'\nпрофессия: {job}'
                   f'\nсайт: {site}'
                   f'\nкомпания: {company}')

bot.infinity_polling()
