#!/usr/bin/env python
# -*- coding: utf-8 -*- # строка нужна, чтобы не было ошибки Non-UTF-8 code starting with '\xd1' in file ...

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


import os



bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


Monday = '1) Алгебра(углубленная) \n2) Алгебра \n3) Литература \n4) Литература \n5) Иностранный язык \n6) Информатика(углубленная) / История(углубленная) / Право(база) / Биология(углубленная) \n7) Информатика(углубленная) / История(углубленная) / Право(база) / Биология(углубленная) \n8) Классный час'
Tuesday = '1) Общество(практика) \n2) Физика(практика) \n3) Алгебра \n4) Геометрия \n5) Русский язык \n6) Русский язык \n7) Генетика/Биология(база) \n8) Генетика'
Wednesday = '1) --- \n2) Алгебра \n3) История \n4) История \n5) Астрономия \n6) ОБЖ \n7) Химия(углубленная) / Физика(углубленная) / Экономика(база) \n8) Химия(углубленная)'
Thursday = '1) --- \n2) Геометрия(база) / Физика(практика) \n3) Литература \n4) Литература(электив) \n5) Физика(углубленная) / География / МХК / экология \n6) Иностранный язык \n7) Химия(база) / Черчение / Иностранный язык(углубленный)'
Friday = '1) Экономические задачи \n2) Геометрия(углубленная) / Геометрия(профильная) \n3) Общество(углубленное) / Физика(углубленная) / Биология(углубленная) \n4) Общество(углубленное) / Физика(углубленная) / Биология(углубленная) \n5) Информатика(углубленная) / Физика(база) / География / Право(углубленное) \n6) Русский язык \n7) Информатика(углубленная) / Физика(база) / География / Право(углубленное) \n8) Химия(углубленная) \n9) Химия(углубленная)'
Saturday = '1) Иностранный язык(углубленный) / Физкультура(1 группа) \n2) Иностранный язык(углубленный) / Физкультура(1 группа) \n3) Программирование / Экономика(углубленная) / Физкультура(2 группа) \n4) Программирование / Экономика(углубленная) / Физкультура(2 группа) \n5) Алгебра(углубленная) / Алгебра(профильная) \n6) Алгебра(углубленная) / Алгебра(профильная)'
'''*******************************УЧЕНИЧЕСКАЯ ЧАСТЬ************************************************'''
@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здраствуй искатель истины \nДля того чтобы узнать расписание на один из дней введите нужную команду: \n Понедельник:  /расписание_пн \n Вторник:  /расписание_вт \n Среда:  /расписание_ср \n Четверг:  /расписание_чт \n Пятница:  /расписание_пт \n Суббота:  /расписание_сб ')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/https://t.me/School_hackathon_Bot')    

@dp.message_handler(commands=['расписание_пн'])
async def command_Monday(message : types.Message):
    await bot.send_message(message.from_user.id, Monday)
@dp.message_handler(commands=['расписание_вт'])
async def command_Tuesday(message : types.Message):
    await bot.send_message(message.from_user.id, Tuesday)
@dp.message_handler(commands=['расписание_ср'])
async def command_Wednesday(message : types.Message):
    await bot.send_message(message.from_user.id, Wednesday)
@dp.message_handler(commands=['расписание_чт'])
async def command_Thursday(message : types.Message):
    await bot.send_message(message.from_user.id, Thursday)
@dp.message_handler(commands=['расписание_пт'])
async def command_Friday(message : types.Message):
    await bot.send_message(message.from_user.id, Friday)
@dp.message_handler(commands=['расписание_сб'])
async def command_Saturday(message : types.Message):
    await bot.send_message(message.from_user.id, Saturday)

    #await message.reply(message.text)
    #await message.reply(message.text)
    #await bot.send_message(message.from_user.id, message.text)








executor.start_polling(dp, skip_updates=True)