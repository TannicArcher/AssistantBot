
from aiogram import types
import datetime
import random
import requests
import json
import time

import message
import config

from utils.mydb import *
from utils.user import User


async def first_join(user_id, username, code, bot):
    conn, cursor = connect()
    
    cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"')
    row = cursor.fetchall()

    if len(row) == 0:
        users = [f'{user_id}', f'{username}', '0', '0', '0', '0', '0', '0', '0', f'{datetime.datetime.now()}', 'False']
        cursor.execute(f'INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?,?)', users)
        conn.commit()

        return True
        
    return False


def days_stats_users(day):
    start = day
    a = start.split('-')
    aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
    bb = datetime.date.today()
    cc = bb - aa
    dd = str(cc)
    ss = dd.split()[0]

    return ss

def cheked_days(day):
    if day.split(':')[0] == '0':
        return '0'
    else:
        return day

def click_url(url):
    urls = f'https://clck.ru/--?url={url}'
    url = f"https://uni.su/api/?url={url}"
    url2 = f"https://is.gd/create.php?format=simple&url={url}"
    url3 = f"https://v.gd/create.php?format=simple&url={url}"
    r1 = requests.get(urls).text
    r2 = requests.get(url).text
    r3 = requests.get(url2).text
    r4 = requests.get(url3).text

    return r1, r2, r3, r4

def count_short(user_id, value):
    conn, cursor = connect()

    cursor.execute(f'UPDATE users SET short = short + {value} WHERE user_id = "{user_id}"')
    conn.commit()
    conn.close()

def type_proxy(typ: int) -> str:
    string = {
            1:"socks5", 2:"socks4", 3:"http"
    }

    p = requests.get("http://d4n13l3k00.ml/api/proxy/" + string[typ] + "?c=5").json()

    return p

def count_proxy(user_id, value):
    conn, cursor = connect()

    cursor.execute(f'UPDATE users SET proxies = proxies + {value} WHERE user_id = "{user_id}"')
    conn.commit()
    conn.close()

def count_password(user_id, value):
    conn, cursor = connect()

    cursor.execute(f'UPDATE users SET gen_pass = gen_pass + {value} WHERE user_id = "{user_id}"')
    conn.commit()
    conn.close()

def count_login(user_id, value):
    conn, cursor = connect()

    cursor.execute(f'UPDATE users SET gen_name = gen_name + {value} WHERE user_id = "{user_id}"')
    conn.commit()
    conn.close()

def count_screen(user_id, value):
    conn, cursor = connect()

    cursor.execute(f'UPDATE users SET screen = screen + {value} WHERE user_id = "{user_id}"')
    conn.commit()
    conn.close()

def add_temp_mail(user_id, email, date):
    conn, cursor = connect()

    mail = [f"{user_id}", f"{email}", f"{date}"]
    cursor.execute("INSERT INTO temp_mails VALUES (?,?,?)", mail)
    conn.commit()
    conn.close()

def select_temp_mail(user_id):
    conn, cursor = connect()

    row = cursor.execute(f"SELECT email, date FROM temp_mails WHERE user_id = '{user_id}'").fetchall()
    conn.close()

    return row

def add_email_history(user_id, email):
    conn, cursor = connect()

    mail = [f"{user_id}", f"{email}"]
    cursor.execute(f"INSERT INTO email_history VALUES (?,?)", mail)
    conn.commit()
    conn.close()

def select_email_history(user_id):
    conn, cursor = connect()

    row = cursor.execute(f"SELECT email FROM email_history WHERE user_id = '{user_id}'").fetchall()
    conn.close()

    return row

def check_ip(ip):
    r = requests.get(f"https://api.ipdata.co/{ip}?api-key=7149ffee49a432bb1c7557e3235afdf78a2d22fcdde3a4ecd7a5d5ca")
    data = json.loads(r.text)

    city = str(data['city'])
    region = str(data['region'])
    country_name = str(data['country_name'])
    country_code = str(data['country_code'])
    continent_name = str(data['continent_name'])
    continent_code = str(data['continent_code'])
    calling_code = str(data['calling_code'])
    latitude = str(data['latitude'])
    longitude = str(data['longitude'])
    postal = str(data['postal'])
    time_zone = str(data['time_zone']['name'])
    time_zone2 = str(data['time_zone']['current_time'])
    currency = str(data['currency']['name'])
    currency2 = str(data['currency']['code'])

    return city, region, country_name, country_code, continent_name, continent_code, calling_code, latitude, longitude, postal, time_zone, time_zone2, currency, currency2


def stats_bot():
    conn, cursor = connect()

    proxy = cursor.execute('SELECT SUM(proxies) from users').fetchall()[0][0]
    password = cursor.execute('SELECT SUM(gen_pass) from users').fetchall()[0][0]
    nick = cursor.execute('SELECT SUM(gen_name) from users').fetchall()[0][0]
    screen = cursor.execute('SELECT SUM(screen) from users').fetchall()[0][0]
    shorts = cursor.execute('SELECT SUM(short) from users').fetchall()[0][0]
    email = cursor.execute('SELECT SUM(gen_mail) from users').fetchall()[0][0]
    conn.close()


    return int(proxy), password, nick, screen, shorts, email

def count_mail(user_id, value):
    conn, cursor = connect()

    cursor.execute(f'UPDATE users SET gen_mail = gen_mail + {value} WHERE user_id = "{user_id}"')
    conn.commit()
    conn.close()