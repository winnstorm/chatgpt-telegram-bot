import os
import openai
from aiogram import Bot, Dispatcher, executor, types

Bot = Bot(token = 'put your Telegram bot token here')
dp = Dispatcher(Bot)

# here we define the openai api key
openai.api_key = 'put your openai api key here'

@dp.message_handler(commands = ['start','help'])
async def welcome(message: types.Message):
    await message.reply('Hola ! Soy Gabefana tu Bot Inteligente... preguntame lo que quieras saber')

@dp.message_handler()
async def gpt(message: types.Message):
    response = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = message.text,
        temperature = 0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    await message.reply(response.choices[0].text)

if __name__ == '__main__':
    executor.start_polling(dp)