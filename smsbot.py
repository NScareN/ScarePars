#!/bin/env python3
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import configparser
import os, sys
import csv
import random
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
SLEEP_TIME = 30

class main():

    def banner():
        print(f"""
    {re}╔═╗╔═╗╔═╗╔═╗╔══{cy}╔═╗╔═╗╔═╗╔═╗
    {re}╚═╗║  ╠═╣╠╦╝╠══{cy}╠═╝╠═╣╠╦╝╚═╗
    {re}╚═╝╚═╝╩ ╩╩╚═╚══{cy}╩  ╩ ╩╩╚═╚═╝
            """)

    def send_sms():
        try:
            cpass = configparser.RawConfigParser()
            cpass.read('config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
        except KeyError:
            os.system('clear')
            main.banner()
            print(re+"[!] Для начала, запустите setup.py\n")
            sys.exit(1)

        client = TelegramClient(phone, api_id, api_hash)
         
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            os.system('clear')
            main.banner()
            client.sign_in(phone, input(gr+'[+] Введите код: '+re))
        
        os.system('clear')
        main.banner()
        #input_file = "/Users/sergejstolin/PythonProg/TGPars-main/members.csv"
        m_file = input(gr+"[+] Введите название базы для рассылки: "+re)
        input_file = "databases/"+m_file+".csv"
        print((gr+'[+] Выбрана база ')+(re+ m_file+".csv"))
        users = []
        with open(input_file, encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)
        print(gr+"[1] Сделать рассылку по userID\n[2] Сделать рассылку по имени")
        mode = int(input(gr+"Выберите : "+re))
         
        messagesample = open('message.txt')
        message = messagesample.read()

        for user in users:
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            else:
                print(re+"[!] Invalid Mode. Exiting.")
                client.disconnect()
                sys.exit()
            try:
                print(gr+"[+] Отправка сообщения: ", re+ user['name'])
                client.send_message(receiver, message.format(user['name']))
                print((gr+"[+] Ожидаю ")+(re+ {})+ (" секунд".format(SLEEP_TIME)))
                time.sleep(1)
            except PeerFloodError:
                print(re+"[!] Получил предупреждение о спаме от Телеграма. \n[!] Скрипт остановлен. \n[!] Повторите через некоторое время.")
                client.disconnect()
                sys.exit()
            except Exception as e:
                print(re+"[!] Ошибка:", e)
                print(re+"[!] Пытаюсь продолжить...")
                continue
        client.disconnect()
        print((gr+"Готово. Сообщение разослано всем пользователям из базы ")+(re+ m_file+".csv"))



main.send_sms()
