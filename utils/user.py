from utils.mydb import *

import config


class User():
    
    def __init__(self, user_id=None, username=None):
        if username != None:
            conn, cursor = connect()

            cursor.execute(f'SELECT * FROM users WHERE username = "{username}"')
            user = cursor.fetchone()

            if user != None:
                user_id = user[0]
            else:
                self.user_id = None
                return

        conn, cursor = connect()
        cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"')
        user = cursor.fetchone()

        self.user_id = user[0]
        self.username = user[1]
        self.proxies = user[2]
        self.short = user[3]
        self.screen = user[4]
        self.ip = user[5]
        self.gen_name = user[6]
        self.gen_pass = user[7]
        self.gen_mail = user[8]
        self.date = user[9]
        self.ban = user[10]



    def update_balance(self, value):
        conn, cursor = connect()
        cursor.execute(f'UPDATE users SET balance = {float(self.balance) + float(value)} WHERE user_id = "{self.user_id}"')
        conn.commit()

        return True


