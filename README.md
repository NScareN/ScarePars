# ScarePars
* <img src=https://img.shields.io/badge/version-1.1.1-blue />
# Установка
* Windows:
  * Скачайте Python 3.8 [здесь](https://www.python.org/downloads/release/python-38)
  * Запустите установщик, нажмите 'add python to PATH'
  * Скачайте `ScarePars`
  * Откройте командную строку в директории `ScarePars`
  * Напишите в командной строке: **python setup.py -i**
  * Затем, перейдите на [my.telegram.org](my.telegram.org) и войдите в свой аккаунт
  * Выберите `API Development Tools`
  * Напишите в командной строке: **python setup.py -c**
  * Введите `api_id`, `api_hash` и `номер телефона`
  
* Termux:
  * **pkg update**
  * **pkg install python3 python3-pip git -y**
  * **git clone `https://github.com/NScareN/ScarePars/`**
  * **cd ScarePars**
  * **python setup.py -i**
  * Затем, перейдите на [my.telegram.org](my.telegram.org) и войдите в свой аккаунт
  * Выберите `API Development Tools`
  * **python setup.py -c**
  * Введите `api_id`, `api_hash` и `номер телефона`
  
* Linux
  * **sudo apt update**
  * **sudo apt install python3 python3-pip git -y**
  * **git clone `https://github.com/NScareN/ScarePars/`**
  * **cd ScarePars**
  * **python setup.py -i**
  * Затем, перейдите на [my.telegram.org](my.telegram.org) и войдите в свой аккаунт
  * Выберите `API Development Tools`
  * В терминале напишите **python setup.py -c**
  * Введите `api_id`, `api_hash` и `номер телефона`
  * !Внимание, если у вас появляются ошибки при исполнении команды apt, возпользуйтесь аналогом в виде Homebrew

# Использование
* Парсинг
  * **python pars.py**
* Рассылка
  * **python smsbot.py**
