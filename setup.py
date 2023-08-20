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
import shutil

def banner():
    os.system('clear')
    print(f"""
    {re}╔═╗╔═╗╔═╗╔═╗╔══{cy}╔═╗╔═╗╔═╗╔═╗
    {re}╚═╗║  ╠═╣╠╦╝╠══{cy}╠═╝╠═╣╠╦╝╚═╗
    {re}╚═╝╚═╝╩ ╩╩╚═╚══{cy}╩  ╩ ╩╩╚═╚═╝
    """)

def requirements():
	def csv_lib():
		banner()
		print(gr+'['+cy+'+'+gr+']'+cy+' Это может занять время...')
		os.system("""
			pip3 install cython numpy pandas
			python3 -m pip install cython numpy pandas
			""")
	banner()
	print(gr+'['+cy+'+'+gr+']'+cy+' Это займет до 10 минут.')
	input_csv = input(gr+'['+cy+'+'+gr+']'+cy+' Хотите включить слияние csv? (y/n): ').lower()
	if input_csv == "y":
		csv_lib()
	else:
		pass
	print(gr+"[+] Устанавливаю компоненты...")
	os.system("""
		pip3 install telethon requests configparser
		python3 -m pip install telethon requests configparser
		touch system/config.data
		""")
	banner()
	print(gr+"[+] Компоненты установлены.\n")


def config_setup():
	import configparser
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

def merge_csv():
	import pandas as pd
	import sys
	banner()
	file1 = pd.read_csv("databases/"+sys.argv[2])
	file2 = pd.read_csv("databases/"+sys.argv[3])
	print(gr+'['+cy+'+'+gr+']'+cy+' Слияние '+sys.argv[2]+' и '+sys.argv[3]+'...')
	print(gr+'['+cy+'+'+gr+']'+cy+' Большие файлы могут потребовать больше времени...')
	merge = file1.merge(file2, on='username')
	mm_file = input(gr+"[+] Введите название базы для сохранения: "+re)
	merge.to_csv("databases/"+mm_file+".csv", index=False)
	print((gr+'['+cy+'+'+gr+']'+cy+' База сохранена как ')+(re+ mm_file)+('.csv'+'\n'))

def update_tool():
	import requests as r
	banner()
	source = r.get("https://raw.githubusercontent.com/NScareN/ScarePars/main/system/version")
	if source.text == '1.1.1':
		print(gr+'['+cy+'+'+gr+']'+cy+' У вас последняя версия')
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

try:
	if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
		print(gr+'['+cy+'+'+gr+']'+cy+' Выбранный модуль: '+re+sys.argv[1])
		config_setup()
	elif any ([sys.argv[1] == '--merge', sys.argv[1] == '-m']):
		print(gr+'['+cy+'+'+gr+']'+cy+' Выбранный модуль: '+re+sys.argv[1])
		merge_csv()
	elif any ([sys.argv[1] == '--update', sys.argv[1] == '-u']):
		print(gr+'['+cy+'+'+gr+']'+cy+' Выбранный модуль: '+re+sys.argv[1])
		update_tool()
	elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
		requirements()
	elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
		banner()
		print("""
	( --config  / -c ) установить конфигурацию API
	( --merge   / -m ) соеденить 2 базы в одну
	( --update  / -u ) обновить инструмент до последней версии
	( --install / -i ) установить компоненты
	( --help    / -h ) показать это сообщение
			""")
	else:
		print('\n'+gr+'['+re+'!'+gr+']'+cy+' Неизвестный аргумент: '+ sys.argv[1])
		print(gr+'['+re+'!'+gr+']'+cy+' Для помощи используйте: ')
		print(gr+'$ python3 setup.py -h'+'\n')
except IndexError:
	print('\n'+gr+'['+re+'!'+gr+']'+cy+' Не выбран аргумент для: '+ sys.argv[1])
	print(gr+'['+re+'!'+gr+']'+cy+' Для помощи используйте: ')
	print(gr+'$ python3 setup.py -h'+'\n')
