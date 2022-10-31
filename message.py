cabinet = """
🖥 Кабинет

<b> Ваш ID:</b>  {user_id}

<b> Ваш ник:</b>  {first_name}

<b> Дней в боте:</b> {date}
Тех. Поддержка ниже:
Слито в @end_software
"""

my_stats = """
<b>📜 Моя статистика:</b>

<b>📨 Использовано почт:</b> {temp_mail}

<b>📸 Скриншотов сделано:</b> {sreen}

<b>✂️ Ссылок сокращено:</b> {short}

<b>🔐 Cгенерировано паролей:</b> {gen_password}

<b>🎴 Cгенерированно ников:</b> {gen_nick}

<b>👻 Прокси сгенерировано:</b> {proxy}
"""

bot_stats = """
<b>📜 CТАТИСТИКА:</b>

<b>📨 Использовано почт:</b> {temp_mail}

<b>📸 Скриншотов сделано:</b> {screens}

<b>✂️ Ссылок сокращено:</b> {shorts}

<b>♻️Генераторы:</b>
<b>👻 Прокси - </b> {proxies}

<b>🔐 Пароли - </b> {passwords}

<b>🎴 Ники - </b> {nicks}
Тех. Поддержка ниже:
Слито в @end_software
"""

info = """
<b>📗 Информация:

Остались вопросы или нужна помощь?

Тех. Поддержка ниже:
Слито в @end_software</b>
"""

hard_pass = """
<b>Вот ваши 5 cложных паролей:</b>

<code>{password}</code>
<code>{password_2}</code>
<code>{password_3}</code>
<code>{password_4}</code>
<code>{password_5}</code>
"""

average_pass = """
<b>Вот ваши 5 средних паролей:</b>

<code>{password}</code>
<code>{password_2}</code>
<code>{password_3}</code>
<code>{password_4}</code>
<code>{password_5}</code>
"""

easy_pass = """
<b>Вот ваши 5 легких паролей:</b>

<code>{password}</code>
<code>{password_2}</code>
<code>{password_3}</code>
<code>{password_4}</code>
<code>{password_5}</code>
"""

gen_logins = """
<b>Cгенерированные логины:</b>

<code>{loguin}</code>
<code>{loguin2}</code>
<code>{loguin3}</code>
"""

ip_adress = """
<b>IP</b> - {ip}

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
<b>Город</b>: <code>{city}</code> | <code>{region}</code>
<b>Страна</b>: <code>{country_name} ({country_code})</code>
<b>Часовой пояс</b>: <code>{time_zone}</code>
<b>Код страны</b>: <code>+{calling_code}</code>
<b>Широта</b>: <code>{latitude}</code> | <b>Долгота</b>: <code>{longitude}</code>
<b>Почтовый индекс</b>: <code>{postal}</code>
<b>Континет</b>: <code>{continent_name} ({continent_code})</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
<b>Валюта</b>: <code>{currency} ({currency2})</code>
<b>Точное время</b>: <code>{time_zone2}</code>
"""