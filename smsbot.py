from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import configparser
import os
import sys
import csv
import time

re = "\033[1;31m"
ye = "\033[1;33m"
gr = "\033[1;32m"
cy = "\033[1;36m"
SLEEP_TIME = 30


class Main:

    @staticmethod
    def banner():
        with open("system/version", "r") as file:
            banner_ver = file.read()
        print(f"{re}╔═╗╔═╗╔═╗╔═╗╔══{cy}╔═╗╔═╗╔═╗╔═╗")
        print(f"{re}╚═╗║  ╠═╣╠╦╝╠══{cy}╠═╝╠═╣╠╦╝╚═╗")
        print(f"{re}╚═╝╚═╝╩ ╩╩╚═╚══{cy}╩  ╩ ╩╩╚═╚═╝ " + "v" + banner_ver + "\n")

    @staticmethod
    def send_sms():
        try:
            cpass = configparser.RawConfigParser()
            cpass.read('system/config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
            if api_id == '':
                os.system('clear')
                Main.banner()
                print(re + "[!] Конфиг повреждён или не обнаружен")
                input(gr + '[' + cy + '+' + gr + ']' + cy + " Вернитесь в главное меню и запустите настройку конфига\n")
                import start
                start.start_up()
            if api_hash == '':
                os.system('clear')
                Main.banner()
                print(re + "[!] Конфиг повреждён или не обнаружен")
                input(gr + '[' + cy + '+' + gr + ']' + cy + " Вернитесь в главное меню и запустите настройку конфига\n")
                import start
                start.start_up()
            if phone == '':
                os.system('clear')
                Main.banner()
                print(re + "[!] Конфиг повреждён или не обнаружен")
                input(gr + '[' + cy + '+' + gr + ']' + cy + " Вернитесь в главное меню и запустите настройку конфига\n")
                import start
                start.start_up()
        except KeyError:
            os.system('clear')
            Main.banner()
            print(re + "[!] Конфиг повреждён или не обнаружен")
            input(re + "[!] Вернитесь в главное меню и запустите настройку конфига\n")
            import start
            start.start_up()

        client = TelegramClient(phone, api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            os.system('clear')
            Main.banner()
            client.sign_in(phone, input(gr + '[+] Введите код: ' + re))

        os.system('clear')
        Main.banner()
        print(gr + '[+] Доступные базы данных:' + re)
        print(os.listdir('databases/'))
        m_file = input(gr + "[" + ye + "!" + gr + "] Введите название базы для рассылки: " + re)
        input_file = "databases/" + m_file + ".csv"
        while os.path.isfile(input_file):
            print((gr + '[+] Выбрана база ') + (re + m_file + ".csv"))
            users = []
            with open(input_file, encoding='UTF-8') as f:
                rows = csv.reader(f, delimiter=",", lineterminator="\n")
                next(rows, None)
                for row in rows:
                    user = {'username': row[0], 'id': int(row[1]), 'access_hash': int(row[2]), 'name': row[3]}
                    users.append(user)
            print(gr + "[1] Сделать рассылку по userID\n[2] Сделать рассылку по имени")
            mode = int(input(gr + "Выберите : " + re))

            print(gr + '[+] Доступные сообщения:' + re)
            print(os.listdir('messages/'))
            t_file = input(gr + "[+] Выберите сообщение для рассылки: " + re)
            messagesample = open("messages/" + t_file + ".txt")
            print((gr + '[+] Выбрано сообщение ') + (re + t_file + ".txt"))
            message = messagesample.read()
            print(gr + "[+] Установите время между отправкой сообщений (в секундах):")
            SLEEP_TIME = int(input(gr + "[+] (По-умолчанию 30 секунд) : " + re))

            for user in users:
                if mode == 2:
                    if user['username'] == "":
                        continue
                    receiver = client.get_input_entity(user['username'])
                elif mode == 1:
                    receiver = InputPeerUser(user['id'], user['access_hash'])
                else:
                    print(re + "[!] Invalid Mode. Exiting.")
                    client.disconnect()
                    sys.exit()
                try:
                    print(gr + "[+] Отправка сообщения: ", re + user['name'])
                    client.send_message(receiver, message.format(user['name']))
                    print((gr + "[+] Ожидаю ") + (re + {}) + (" секунд".format(SLEEP_TIME)))
                    time.sleep(1)
                except PeerFloodError:
                    print(
                        re + "[!] Получил предупреждение о спаме от Телеграма. \n[!] Скрипт остановлен. \n[!] Повторите через некоторое время.")
                    client.disconnect()
                    sys.exit()
                except Exception as e:
                    print(re + "[!] Ошибка:", e)
                    print(re + "[!] Пытаюсь продолжить...")
                    continue
            os.system('clear')
            Main.banner()
            client.disconnect()
            print((gr + "[+] Готово. Сообщение разослано всем пользователям из базы ") + (re + m_file + ".csv"))
            input(gr + '[' + cy + '+' + gr + ']' + cy + ' Вернуться в главное меню ')
            import start
            start.start_up()
        else:
            client.disconnect()
            print((gr + "\n[" + re + "!" + gr + "] Указанная база данных не найдена"))
            print((cy + "[" + re + "1" + cy + "]" + " Повторить"))
            print((cy + "[" + re + "2" + cy + "]" + " В главное меню"))
            c_func = input(gr + '[' + cy + '+' + gr + ']' + cy + ' Выберите действие: ' + re)
            if c_func == "1":
                Main.send_sms()
            if c_func == "2":
                import start
                start.start_up()
            else:
                import start
                start.start_up()


Main.send_sms()
