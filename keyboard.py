from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.mydb import *
import config

main_menu_btn = [
	'🧿 Меню',
	'🖥Кабинет',
	'⛩ Помощь ⛩',
]

def main_menu():
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add(main_menu_btn[0], main_menu_btn[1])
	markup.add(main_menu_btn[2])

	return markup
    


def cabinet_markup():
	markup = InlineKeyboardMarkup(
		inline_keyboard = [
			[
				InlineKeyboardButton(text = '📊 Моя Статистика', callback_data = 'my_stats'),
			]
		]
	)

	return markup


def help_markup():
	markup = InlineKeyboardMarkup(
		inline_keyboard = [
			[
				InlineKeyboardButton(text = '🏆 Cтатитика бота', callback_data = 'stats_for_bot'),
			],
			[
				InlineKeyboardButton(text = '🧑🏻‍💻 Тех. Поддержка', url = config.config("admin_link")),
			]
		]
	)

	return markup


def menu_markup():
	markup = InlineKeyboardMarkup(
		inline_keyboard = [
			[
				InlineKeyboardButton(text = '📷 Скриншот сайта', callback_data = 'screen'),
				InlineKeyboardButton(text = '♻️ Генератор', callback_data = 'generator'),
			],
			[
				InlineKeyboardButton(text = '📩 Временная почта', callback_data = 'temp_mail'),
			],
			[
				InlineKeyboardButton(text = '✂️ Сократитель', callback_data = 'short'),
				InlineKeyboardButton(text = '⛓ Парсер', callback_data = 'parser_group'),
				InlineKeyboardButton(text = '🕹 Пробив IP', callback_data = 'search_ip'),
			],
		]
	)

	return markup

def to_cabinet():
	markup = InlineKeyboardMarkup(
		inline_keyboard = [
			[
				InlineKeyboardButton(text = '🔙 Назад', callback_data = 'to_cabinet'),
			]
		]
	)

	return markup

def email_markup():
	markup = InlineKeyboardMarkup(
		inline_keyboard = [
			[
				InlineKeyboardButton(text = '📬 Проверить письма', callback_data = 'check_mail'),
			],
			[
				InlineKeyboardButton(text = '💢 Отменить почту', callback_data = 'close_mail'),
			]
		]
	)

	return markup

def gen_markup():
	markup = InlineKeyboardMarkup(
		inline_keyboard = [
			[
				InlineKeyboardButton(text = '🔑 Генератор паролей', callback_data = 'gen_passwords'),
			],
			[
				InlineKeyboardButton(text = '🔗 Генератор логинов', callback_data = 'gen_logins'),
			],
			[
				InlineKeyboardButton(text = '⛓ Генератор прокси', callback_data = 'gen_proxies'),
			]
		]
	)

	return markup

def passwords_markup():
	markup = InlineKeyboardMarkup(
		inline_keyboard = [
			[
				InlineKeyboardButton(text = '💣 Cложный', callback_data = 'hard_passwords'),
			],
			[
				InlineKeyboardButton(text = '🧨 Средний', callback_data = 'average_passwords'),
			],
			[
				InlineKeyboardButton(text = '🔫 Легкий', callback_data = 'easy_passwords'),
			]
		]
	)

	return markup

def proxy_markup():
	markup = InlineKeyboardMarkup(
		inline_keyboard = [
			[
				InlineKeyboardButton(text = '💈 Socks 5', callback_data = 'Socks5_proxy'),
			],
			[
				InlineKeyboardButton(text = '💈 Socks 4', callback_data = 'Socks4_proxy'),
			],
			[
				InlineKeyboardButton(text = '💈 HTTP', callback_data = 'http_proxy'),
			]
		]
	)

	return markup

def close():
	markup = InlineKeyboardMarkup(
		inline_keyboard = [
			[
				InlineKeyboardButton(text = '💢 Закрыть', callback_data = 'to_close'),
			]
		]
	)

	return markup