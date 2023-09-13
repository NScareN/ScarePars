import os
import sys

import requests as r

re = "\033[1;31m"
ye = "\033[1;33m"
gr = "\033[1;32m"
cy = "\033[1;36m"


def banner():
    with open("system/version", "r") as file:
        banner_ver = file.read()
    try:
        source = r.get("https://raw.githubusercontent.com/NScareN/ScarePars/main/system/version")
        if source.text > banner_ver:
            print(f"{re}╔═╗╔═╗╔═╗╔═╗╔══{cy}╔═╗╔═╗╔═╗╔═╗")
            print(f"{re}╚═╗║  ╠═╣╠╦╝╠══{cy}╠═╝╠═╣╠╦╝╚═╗")
            print(f"{re}╚═╝╚═╝╩ ╩╩╚═╚══{cy}╩  ╩ ╩╩╚═╚═╝ " + "v" + banner_ver + f" {ye}[доступно обновление]" + "\n")
        else:
            print(f"{re}╔═╗╔═╗╔═╗╔═╗╔══{cy}╔═╗╔═╗╔═╗╔═╗")
            print(f"{re}╚═╗║  ╠═╣╠╦╝╠══{cy}╠═╝╠═╣╠╦╝╚═╗")
            print(f"{re}╚═╝╚═╝╩ ╩╩╚═╚══{cy}╩  ╩ ╩╩╚═╚═╝ " + "v" + banner_ver + "\n")
    except r.exceptions.SSLError:
        print(f"{re}╔═╗╔═╗╔═╗╔═╗╔══{cy}╔═╗╔═╗╔═╗╔═╗")
        print(f"{re}╚═╗║  ╠═╣╠╦╝╠══{cy}╠═╝╠═╣╠╦╝╚═╗")
        print(f"{re}╚═╝╚═╝╩ ╩╩╚═╚══{cy}╩  ╩ ╩╩╚═╚═╝ " + "v" + banner_ver + "\n")


def start_up():
    os.system('clear')
    banner()
    print((cy + "[" + re + "1" + cy + "]" + " рассылка"))
    print((cy + "[" + re + "2" + cy + "]" + " парсинг"))
    print((cy + "[" + gr + "+" + cy + "]" + " Доступные функции:"))
    print((cy + "[" + re + "3" + cy + "]" + " настройка конфига"))
    print((cy + "[" + re + "4" + cy + "]" + " обновление скрипта"))
    print((cy + "[" + re + "5" + cy + "]" + " выход"))
    c_func = input(cy + "[" + gr + "+" + cy + "]" + " Выберите нужную функцию: " + re)
    if c_func == "1":
        import smsbot
        smsbot.Main.send_sms()
    if c_func == "2":
        import pars
        pars.main.parser()
    if c_func == "3":
        import setup
        setup.requirements()
        setup.config_setup()
    if c_func == "4":
        import setup
        setup.update_tool()
    if c_func == "5":
        os.system('clear')
        sys.exit()
    else:
        start_up()


start_up()
