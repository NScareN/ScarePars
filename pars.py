from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import os, sys
import configparser
import csv
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

class main():

    def banner():
        with open("system/version", "r") as file:
            banner_ver = file.read()
        print(f"{re}╔═╗╔═╗╔═╗╔═╗╔══{cy}╔═╗╔═╗╔═╗╔═╗")
        print(f"{re}╚═╗║  ╠═╣╠╦╝╠══{cy}╠═╝╠═╣╠╦╝╚═╗")
        print(f"{re}╚═╝╚═╝╩ ╩╩╚═╚══{cy}╩  ╩ ╩╩╚═╚═╝ " + "v" + banner_ver + "\n")

    def parser():

        try:
            cpass = configparser.RawConfigParser()
            cpass.read('system/config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
            if api_id == '':
                os.system('clear')
                main.banner()
                print(re+"[!] Конфиг повреждён или не обнаружен")
                input(gr+'['+cy+'+'+gr+']'+cy+" Вернитесь в главное меню и запустите настройку конфига\n")
                import start
                start.start_up()
            if api_hash == '':
                os.system('clear')
                main.banner()
                print(re+"[!] Конфиг повреждён или не обнаружен")
                input(gr+'['+cy+'+'+gr+']'+cy+" Вернитесь в главное меню и запустите настройку конфига\n")
                import start
                start.start_up()
            if phone == '':
                os.system('clear')
                main.banner()
                print(re+"[!] Конфиг повреждён или не обнаружен")
                input(gr+'['+cy+'+'+gr+']'+cy+" Вернитесь в главное меню и запустите настройку конфига\n")
                import start
                start.start_up()
        except KeyError:
            os.system('clear')
            main.banner()
            print(re+"[!] Конфиг повреждён или не обнаружен")
            input(re+"[!] Вернитесь в главное меню и запустите настройку конфига\n")
            import start
            start.start_up()
        client = TelegramClient(phone, api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            os.system('clear')
            main.banner()
            client.sign_in(phone, input(gr+'[+] Введите код: '+re))

        os.system('clear')
        main.banner()
        chats = []
        last_date = None
        chunk_size = 200
        groups=[]
 
        result = client(GetDialogsRequest(
                    offset_date=last_date,
                    offset_id=0,
                    offset_peer=InputPeerEmpty(),
                    limit=chunk_size,
                    hash = 0
                ))
        chats.extend(result.chats)
 
        for chat in chats:
            try:
                if chat.megagroup== True:
                    groups.append(chat)
            except:
                continue
 
        print(gr+'[+] Доступные группы для парсинга:'+re)
        i=0
        for g in groups:
            print(gr+'['+cy+str(i)+gr+']'+cy+' - '+ g.title)
            i+=1
 
        print('')
        g_index = input(gr+"[+] Введите номер группы для выбора: "+re)
        try:
            target_group=groups[int(g_index)]
        except (IndexError, ValueError):
            client.disconnect()
            print((gr+"\n["+re+"!"+gr+"] Указанная группа не найдена"))
            print((cy+ "[" + re+ "1" + cy+ "]" + " Повторить"))
            print((cy+ "[" + re+ "2" + cy+ "]" + " В главное меню"))
            c_func = input(gr+'['+cy+'+'+gr+']'+cy+' Выберите действие: '+re)
            if c_func == "1":
                main.parser()
            if c_func == "2":
                import start
                start.start_up()
            else:
                import start
                start.start_up()

        g_name = target_group.title
 
        print(gr+'[+] Собираю данные участников...')
        time.sleep(1)
        all_participants = []
        all_participants = client.get_participants(target_group, aggressive=True)
 
        print(gr+'[+] Сохраняю в файл...')
        time.sleep(1)
        m_file = input(gr+"[+] Введите название базы для сохранения: "+re)
        with open("databases/"+m_file+".csv","w",encoding='UTF-8') as f:
            writer = csv.writer(f,delimiter=",",lineterminator="\n")
            writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
            for user in all_participants:
                if user.username:
                    username = user.username
                else:
                    username = ""
                if user.first_name:
                    first_name = user.first_name
                else:
                    first_name = ""
                if user.last_name:
                    last_name= user.last_name
                else:
                    last_name= ""
                name = (first_name + ' ' + last_name).strip()
                if "Bot" in username:
                    writer.writerow('\n')
                else:
                    writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
        file_path = os.path.dirname(__file__)
        os.system('clear')
        main.banner()    
        print((gr+"[+] Участники группы ")+(re+ g_name)+(gr+" сохранены в базу ")+(re+ m_file+".csv"))
        client.disconnect()
        input(gr+'['+cy+'+'+gr+']'+cy+' Вернуться в главное меню ')
        import start
        start.start_up()
main.parser()