#!/bin/env python3

"""

вы можете запустить setup.py заново 
если вы ошиблись

"""
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

import os, sys
import time
import requests as r

with open("system/version", "r") as file:
       banner_ver = file.read()
       
def banner():
    print(f"{re}╔═╗╔═╗╔═╗╔═╗╔══{cy}╔═╗╔═╗╔═╗╔═╗")
    print(f"{re}╚═╗║  ╠═╣╠╦╝╠══{cy}╠═╝╠═╣╠╦╝╚═╗")
    print(f"{re}╚═╝╚═╝╩ ╩╩╚═╚══{cy}╩  ╩ ╩╩╚═╚═╝ " + "v" + banner_ver + "\n")

def requirements():
	os.system('clear')
	banner()
	print(gr+"[+] Устанавливаю компоненты...")
	os.system("""
		pip3 install telethon requests configparser
		python3 -m pip install telethon requests configparser
		pip3 install cython numpy pandas
		python3 -m pip install cython numpy pandas
		touch system/config.data
		""")
	banner()
	print(gr+"[+] Компоненты установлены.\n")


def config_setup():
	import configparser
	os.system('clear')
	banner()
	cpass = configparser.RawConfigParser()
	cpass.add_section('cred')
	xid = input(gr+"[+] Введите api_id: "+re)
	cpass.set('cred', 'id', xid)
	xhash = input(gr+"[+] Введите hash_id: "+re)
	cpass.set('cred', 'hash', xhash)
	xphone = input(gr+"[+] Введите номер телефона: "+re)
	cpass.set('cred', 'phone', xphone)
	setup = open('system/config.data', 'w')
	cpass.write(setup)
	setup.close()
	print(gr+"[+] Установка завершена!")
	input(gr+'['+cy+'+'+gr+']'+cy+' Вернуться в главное меню ')
	import start
	start.start_up()

def update_tool():
	os.system('clear')
	banner()
	try:
		source = r.get("https://raw.githubusercontent.com/NScareN/ScarePars/main/system/version")
	except r.exceptions.SSLError:
		print(gr+'['+re+'!'+gr+']'+cy+' Нет связи с сервером (попробуйте включить VPN)\n')
		input(gr+'['+cy+'+'+gr+']'+cy+' Вернуться в главное меню ')
		import start
		start.start_up()
	if source.text == banner_ver or source.text < banner_ver:
		print(gr+'['+cy+'+'+gr+']'+cy+' У вас последняя версия ' + '(' +re + banner_ver +cy +')')
		input(gr+'['+cy+'+'+gr+']'+cy+' Вернуться в главное меню ')
		import start
		start.start_up()
	else:
		print(gr+'['+cy+'+'+gr+']'+cy+' Удаляю старые файлы...')
		os.system('rm *.py');time.sleep(3)
		os.system('rm LICENSE');time.sleep(3)
		os.system('rm README.md');time.sleep(3)
		os.system('rm system/version');time.sleep(3)
		print(gr+'['+cy+'+'+gr+']'+cy+' Получаю файлы обновления...')
		os.system("""
			curl -s -O https://raw.githubusercontent.com/NScareN/ScarePars/main/pars.py
			curl -s -O https://raw.githubusercontent.com/NScareN/ScarePars/main/setup.py
			curl -s -O https://raw.githubusercontent.com/NScareN/ScarePars/main/smsbot.py
			curl -s -O https://raw.githubusercontent.com/NScareN/ScarePars/main/LICENSE
			curl -s -O https://raw.githubusercontent.com/NScareN/ScarePars/main/README.md
			curl -s -O https://raw.githubusercontent.com/NScareN/ScarePars/main/system/version
			chmod 777 *.py
			""");time.sleep(3)
		os.replace("version", "system/version")
		print(gr+'\n['+cy+'+'+gr+']'+cy+' Обновление завершено.\n')
		input(gr+'['+cy+'+'+gr+']'+cy+' Вернуться в главное меню ')
		import start
		start.start_up()


def update_check():
	os.system('clear')
	banner()
	source = r.get("https://raw.githubusercontent.com/NScareN/ScarePars/main/system/version")
	if source.text == banner_ver or source.text < banner_ver:
		print(gr+'['+cy+'+'+gr+']'+cy+' У вас последняя версия ' + '(' +re + banner_ver +cy + ')')
	else:
		print(gr+'['+cy+'+'+gr+']'+cy+' Ваша версия: ' +re + 'v' + banner_ver)
		print(gr+'['+cy+'+'+gr+']'+cy+' Последняя доступная версия: ' +re + 'v' + source.text)

try:
	if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
		print(gr+'['+cy+'+'+gr+']'+cy+' Выбранный модуль: '+re+sys.argv[1])
		config_setup()
	elif any ([sys.argv[1] == '--update', sys.argv[1] == '-u']):
		print(gr+'['+cy+'+'+gr+']'+cy+' Выбранный модуль: '+re+sys.argv[1])
		update_tool()
	elif any ([sys.argv[1] == '--updatecheck', sys.argv[1] == '-uc']):
		print(gr+'['+cy+'+'+gr+']'+cy+' Выбранный модуль: '+re+sys.argv[1])
		update_check()
	elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
		requirements()
	elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
		banner()
		print("""
	( --config      /  -c  ) установить конфигурацию API
	( --update      /  -u  ) обновить инструмент до последней версии
	( --updatecheck /  -uc ) проверить наличие обновлений
	( --install     /  -i  ) установить компоненты
	( --help        /  -h  ) показать это сообщение
			""")
	else:
		print('\n'+gr+'['+re+'!'+gr+']'+cy+' Неизвестный аргумент: '+ sys.argv[1])
		print(gr+'['+re+'!'+gr+']'+cy+' Для помощи используйте: ')
		print(gr+'$ python3 setup.py -h'+'\n')
except IndexError:
		print('\n'+gr+'['+re+'!'+gr+']'+cy+' Не выбран аргумент')
		print(gr+'['+re+'!'+gr+']'+cy+' Для помощи используйте: ')
		print(gr+'$ python3 setup.py -h'+'\n')
