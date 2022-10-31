from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from time import sleep
import random
import time
import asyncio
import requests
import datetime
import re
import threading

import config
import message as m
import functions as func
import keyboard as menu
from states import *
from utils.user import *
from utils.logger import *
from utils.randomizer import *
from utils.temp_mail import *
from utils.parser import *
from states import *
from filters.chat_filters import IsGroup, IsPrivate


bot = Bot(token = config.config('bot_token'), parse_mode = types.ParseMode.HTML)
storage = MemoryStorage()

vip = Dispatcher(bot, storage = storage)



@vip.message_handler(IsPrivate(), Command(commands = ['start', 'help']))
async def start_handler(msg: types.Message):
	check = await func.first_join(user_id = msg.from_user.id, username = msg.from_user.username, code = msg.text, bot = bot)
	if check == True:
		await msg.answer(f'<b>Добро пожаловать {msg.from_user.get_mention(as_html=True)}!</b>'
						 f'<b>Я Assistant, чекай меню, у меня много классных приколюшек!</b>', 
						reply_markup = menu.main_menu())
		await bot.send_message(chat_id = config.config('admin_group'),
							text = f'Новый пользователь {msg.from_user.get_mention(as_html=True)}')
	else:
		await msg.answer(f'<b>Добро пожаловать {msg.from_user.get_mention(as_html=True)}!</b>'
						 f'<b>Я Assistant, чекай меню, у меня много классных приколюшек!</b>',
						reply_markup = menu.main_menu())



@vip.message_handler(IsPrivate(), content_types = ['text'])
async def message_handler(msg: types.Message):
	chat_id = msg.from_user.id

	try:
		if User(chat_id).ban == 'False':

			if msg.text in menu.main_menu_btn[0]:
				await bot.send_message(
					chat_id = chat_id,
					text = '<b>Выбери нужную тебе функцию:</b>',
					reply_markup = menu.menu_markup())

			if msg.text in menu.main_menu_btn[1]:
				try:
					i = User(chat_id)
					await bot.send_message(
						chat_id = chat_id,
						text = m.cabinet.format(
							user_id = chat_id,
							first_name = msg.from_user.get_mention(as_html=True),
							date = func.cheked_days(func.days_stats_users(i.date[:10]))),
						reply_markup = menu.cabinet_markup())
				except:
					await msg.answer('Ошибка! /start')

			elif msg.text in menu.main_menu_btn[2]:
				await bot.send_message(
					chat_id = chat_id,
					text = m .info,
					reply_markup = menu.help_markup())
	except Exception as e:
		logger.error(f'ERROR: {e}')


@vip.callback_query_handler()
async def handler_call(call: types.CallbackQuery, state: FSMContext):
    chat_id = call.from_user.id
    message_id = call.message.message_id

    if User(chat_id).ban == 'False':

    	if call.data == 'my_stats':
    		try:
    			i = User(chat_id)
    			await bot.edit_message_text(chat_id = chat_id,
    						message_id = message_id,
    						text = m.my_stats.format(
    								short = i.short,
    								temp_mail = i.gen_mail,
    								sreen = i.screen,
    								gen_password = i.gen_pass,
    								gen_nick = i.gen_name,
    								proxy = i.proxies),
    						reply_markup = menu.to_cabinet())
    		except Exception as e:
    			logger.error(f'ERROR: {e}')

    	if call.data == 'to_cabinet':
    		try:
    			await bot.edit_message_text(chat_id = chat_id,
    						message_id = message_id,
    						text = m.cabinet.format(
    							user_id = chat_id,
    							first_name = call.from_user.get_mention(as_html=True),
    							date = func.cheked_days(func.days_stats_users(User(chat_id).date[:10]))),
    						reply_markup = menu.cabinet_markup())
    		except Exception as e:
    			pass

    	if call.data == 'stats_for_bot':
    		info = func.stats_bot()
    		await bot.edit_message_text(chat_id = chat_id, message_id = message_id,
    							text = m.bot_stats.format(
    									proxies = info[0],
    									passwords = info[1],
    									nicks = info[2],
    									screens = info[3],
    									shorts = info[4],
    									temp_mail = info[5]),
    							reply_markup = menu.help_markup())

    	if call.data == 'short':
    		await CutterLink.link.set()
    		await bot.send_message(chat_id = chat_id,
    			text = '<b>Пришли ссылку!\n\nПример:</b> <code>https://google.com/</code>')

    	if call.data == 'generator':
    		await bot.edit_message_text(chat_id = chat_id, message_id = message_id,
    					text = f'<b>Выбери генератор:</b>', reply_markup = menu.gen_markup())

    	if call.data == 'gen_passwords':
    		await bot.edit_message_text(chat_id = chat_id, message_id = message_id,
    					text = f'<b>Выбери сложность пароля</b>', reply_markup = menu.passwords_markup())

    	if call.data == 'hard_passwords':
    		func.count_password(chat_id, 1)
    		await bot.edit_message_text(chat_id = chat_id, message_id = message_id,
    					text = m.hard_pass.format(
    							password = hard_pass(16), password_2 = hard_pass(16),
    							password_3 = hard_pass(16), password_4 = hard_pass(16),
    							password_5 = hard_pass(16)), 
    					reply_markup = menu.passwords_markup())

    	if call.data == 'average_passwords':
    		func.count_password(chat_id, 1)
    		await bot.edit_message_text(chat_id = chat_id, message_id = message_id,
    					text = m.average_pass.format(
    							password = medium_pass(12), password_2 = medium_pass(12),
    							password_3 = medium_pass(12), password_4 = medium_pass(12),
    							password_5 = medium_pass(12)), 
    					reply_markup = menu.passwords_markup())

    	if call.data == 'easy_passwords':
    		func.count_password(chat_id, 1)
    		await bot.edit_message_text(chat_id = chat_id, message_id = message_id,
    					text = m.easy_pass.format(
    							password = easy_pass(8), password_2 = easy_pass(8),
    							password_3 = easy_pass(8), password_4 = easy_pass(8),
    							password_5 = easy_pass(8)), 
    					reply_markup = menu.passwords_markup())

    	if call.data == 'gen_proxies':
    		await bot.edit_message_text(chat_id = chat_id, message_id = message_id,
    					text = f'<b>Выбери тип прокси:</b>', reply_markup = menu.proxy_markup())

    	if call.data == 'Socks5_proxy':
    		proxy = func.type_proxy(1)
    		if '.' in proxy[0] and ':' in proxy[0]:
    			func.count_proxy(chat_id, 1)
    			await bot.delete_message(chat_id, message_id)
    			await bot.send_message(chat_id = chat_id,
    					text = f'<b>Прокси Socks 5</b>\n\n'
    						   f'<code>{proxy[0]}</code>\n'
    						   f'<code>{proxy[1]}</code>\n'
    						   f'<code>{proxy[2]}</code>\n'
    						   f'<code>{proxy[3]}</code>\n'
    						   f'<code>{proxy[4]}</code>\n',
    					reply_markup = menu.proxy_markup())

    	if call.data == 'Socks4_proxy':
    		proxy = func.type_proxy(2)
    		if '.' in proxy[0] and ':' in proxy[0]:
    			func.count_proxy(chat_id, 1)
    			await bot.delete_message(chat_id, message_id)
    			await bot.send_message(chat_id = chat_id,
    					text = f'<b>Прокси Socks 4</b>\n\n'
    						   f'<code>{proxy[0]}</code>\n'
    						   f'<code>{proxy[1]}</code>\n'
    						   f'<code>{proxy[2]}</code>\n'
    						   f'<code>{proxy[3]}</code>\n'
    						   f'<code>{proxy[4]}</code>\n',
    					reply_markup = menu.proxy_markup())

    	if call.data == 'http_proxy':
    		proxy = func.type_proxy(3)
    		if '.' in proxy[0] and ':' in proxy[0]:
    			func.count_proxy(chat_id, 1)
    			await bot.delete_message(chat_id, message_id)
    			await bot.send_message(chat_id = chat_id,
    					text = f'<b>Прокси HTTP</b>\n\n'
    						   f'<code>{proxy[0]}</code>\n'
    						   f'<code>{proxy[1]}</code>\n'
    						   f'<code>{proxy[2]}</code>\n'
    						   f'<code>{proxy[3]}</code>\n'
    						   f'<code>{proxy[4]}</code>\n',
    					reply_markup = menu.proxy_markup())

    	if call.data == 'gen_logins':
    		func.count_login(chat_id, 1)
    		await bot.send_message(chat_id = chat_id,
    				text = m.gen_logins.format(
    					loguin = random.choice(open('utils\\names.txt').readlines()),
    					loguin2 = random.choice(open('utils\\names.txt').readlines()),
    					loguin3 = random.choice(open('utils\\names.txt').readlines())),
    				reply_markup = menu.close())

    	if call.data == 'to_close':
    		await bot.delete_message(chat_id = chat_id, message_id = message_id)

    	if call.data == 'screen':
    		await ScreenSite.link.set()
    		await bot.edit_message_text(chat_id = chat_id, message_id = message_id,
    				text = '<b>Кинь ссылку на сайт, я пришлю тебе скриншот!</b>')

    	if call.data == 'search_ip':
    		await SearchIp.ip.set()
    		await call.message.answer('<b>Введи IP, я тебе скажу все о нем</b>')

    	if call.data == 'parser_group':
    		await ParserGroup.chat.set()
    		await bot.edit_message_text(chat_id = chat_id, message_id = message_id, 
    					text = '<b>Кинь ссылку на чат, я спарсю юзеры пользователей</b>')

    	if call.data == 'temp_mail':
    		domains = get_domains()
    		try:
    			if domains["message"]:
    				await bot.edit_message_text(chat_id = chat_id, message_id = message_id,
    							text = '<b>Почты закончились !</b>')
    				await bot.send_message(chat_id = config.config('channel_logs'),
    							text = 'Админ, алло, почты кончились!')
    		except TypeError:
    			mail = get_new_temp_mail(get_domains()[random.randint(1, len(domains)-1)])
    			temp_mail_date = time.time()
    			func.add_temp_mail(chat_id, mail, temp_mail_date)
    			await bot.edit_message_text(chat_id = chat_id, message_id = message_id,
    						text = f'<b>Ваша почта:</b> {mail}', reply_markup = menu.email_markup())
    			await bot.send_message(chat_id = config.config('channel_logs'),
    						text = f'{call.from_user.get_mention(as_html=True)} сгенерировал почту')
    			func.count_mail(chat_id, 1)

    	if call.data == 'check_mail':
    		email = func.select_temp_mail(chat_id)
    		mail_list = get_messages(str(email[0][0]))
    		if mail_list['length'] == 0:
    			history_email = func.select_email_history(chat_id)
    			if str(history_email) == "[]":
    				await bot.delete_message(chat_id, message_id)
    				await bot.send_message(chat_id = chat_id,
    						text = f'<b>Ваша почта:</b> {email[0][0]}\n'
    							   f'<b>Новых сообщений нет</b>',
    						reply_markup = menu.email_markup())
    			else:
    				mails = ""
    				for i in range(len(history_email)):
    					mails += history_email[i][0]
    					mails += "\n\n"
    				await bot.delete_message(chat_id, message_id)
    				await bot.send_message(chat_id = chat_id,
    							text = f'<b>Ваша почта:</b> {email[0][0]}\n'
    								   f'<b>Новых сообщений нет.\nСтарые:</b> {mails}',
    							reply_markup = menu.email_markup())
    		elif mail_list['length'] == 1:
    			mail_id = str(mail_list)[0:9].split("'")[1]
    			mail_text = mail_list[mail_id]["text"]
    			mail_sender_name = mail_list[mail_id]["sender_name"]
    			mail_subject = mail_list[mail_id]['subject']
    			mes = f"\nОт кого - {mail_sender_name}: \nТема сообщения - {mail_subject}\nТекст сообщения - {mail_text}"
    			print(mes)
    			func.add_email_history(call.from_user.id, mes)
    			history_email = func.select_email_history(call.from_user.id)
    			mails = ""
    			for i in range(len(history_email)):
    				mails += history_email[i][0]
    				mails += "\n\n"
    			await bot.delete_message(chat_id, message_id)
    			await bot.send_message(chat_id = chat_id,
    							text = f'<b>Ваша почта:</b> {email[0][0]}\n'
    								   f'<b>Cообщения:</b> {mails}',
    							reply_markup = menu.email_markup())


@vip.message_handler(state = CutterLink.link)
async def Cutter_Link(msg: types.Message, state: FSMContext):
	try:
		url = msg.text
		link = func.click_url(url)
		await bot.send_message(
				chat_id = msg.from_user.id,
				text = f'<b>Вот сокращенные варианты ссылки:</b>\n\n'
					   f'1. {link[0]}\n'
					   f'2. {link[1]}\n'
					   f'3. {link[2]}\n'
					   f'4. {link[3]}\n',
				disable_web_page_preview=True)
		func.count_short(msg.from_user.id, 1)

		await state.finish()
	except Exception as e:
		await msg.answer('Это точно ссылка? Давай нормальную!')
		await state.finish()

@vip.message_handler(state = ScreenSite.link)
async def ScreenshotWebsite(msg: types.Message, state: FSMContext):
	try:
		screen = requests.get(f"https://webshot.deam.io/{msg.text}/?width=1440&height=1024?type=png")
		await bot.send_photo(chat_id = msg.from_user.id,
					photo = screen.content,
					caption = f'<b>Cкриншот сайта:</b> <code>{msg.text}</code>')
		func.count_screen(msg.from_user.id, 1)
		await state.finish()
	except Exception as e:
		await state.finish()
		await msg.answer('Это не ссылка!')

@vip.message_handler(state = SearchIp.ip)
async def SearchIP(msg: types.Message, state: FSMContext):
	try:
		ip = msg.text
		info = func.check_ip(ip)
		await bot.send_message(chat_id = msg.from_user.id,
					text = m.ip_adress.format(
							ip = msg.text,
							city = info[0],
							region = info[1],
							country_name = info[2],
							country_code = info[3],
							time_zone = info[10],
							calling_code = info[6],
							latitude = info[7],
							longitude = info[8],
							postal = info[9],
							continent_name = info[4],
							continent_code = info[5],
							currency = info[12],
							currency2 = info[13],
							time_zone2 = info[11]))
		await state.finish()
	except:
		await state.finish()
		await msg.answer('Кинь нормальное IP, а не чушь какую то')


@vip.message_handler(state = ParserGroup.chat)
async def Parsergroup(msg: types.Message, state: FSMContext):
	try:
		link = msg.text
		await pars_bot(link)
		if 'https://t.me/joinchat/' in link:
			links = link.split('/')[4]
		elif 'https://t.me/' in link:
			links = link.split('/')[3]
		else:
			links = link
		await msg.answer('Парс произведен!')
		with open(f'docs\\chat_{links}.txt', 'rb') as d:
			await bot.send_document(chat_id = msg.from_user.id, 
					document = d,
					caption = 'Вот база')
		with open(f'docs\\chat_{links}.txt', 'rb') as d:
			await bot.send_document(chat_id = config.config('channel_logs'),
						document = d,
						caption = f'Парс чата {link}, пользователем {msg.from_user.get_mention(as_html=True)}')
		await state.finish()
	except Exception as e:
		await state.finish()
		await msg.answer('Убедитесь в правильности ссылки, возмонжо ссылка на канал')


if __name__ == '__main__':
    executor.start_polling(vip, skip_updates=True)