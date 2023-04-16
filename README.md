# Тестовое задание для DigitalFutureSystems

## Есть два варианта запуска проекта: Docker и Локально

# Клонируем проект:
    git clone git@github.com:RomanH98/coddtask.git

## Команды для инициализации проекта выполняем в корне проекта, в папке coddtask. (Команды для локальных действий могут зависить от sudo)

# Запуск используя Docker:

## Используя Makefile(проверен на Ubuntu 22.04):
    sudo make init


## Самостоятельный запуск:
    sudo docker-compose up -d
    
    sudo docker exec -it digfutsys_web flask db init
    
    sudo docker exec -it digfutsys_web flask db migrate

    sudo docker exec -it digfutsys_web flask db upgrade

# Запуск локально:
## Активировать виртуальное окружение:
    python3 -m venv venv
    
    source venv/bin/activate

## Используя Makefile:
    make local-init
    
    make runlocal
## Cамостоятельный запуск:
    
    pip install -r requirements.txt
    
    flask db init
    
    flask db migrate
    
    flask db upgrade
    
    python runner.py

# После инициализации повторная миграция не нужна. Bторой и последующие запуски:
## Запуск используя Docker:

## Используя Makefile:
        
    sudo make run

## Самостоятельный запуск:
    
    sudo docker-compose up -d

# Остановка Docker контейнеров:
## Используя Makefile:
    
    sudo make stop

## Самостоятельная остановка:
    
    sudo docker stop digfutsys_db
    
    sudo docker stop digfutsys_web

# Запуск локально:
	
## Используя Makefile:
    
    make runlocal
	
## Самостоятельно:
    
    python runner.py

# Проверка задания:
Проверка в POSTMAN:

Метод 1) Осуществляет поиск групп (сообществ) по подстроке и (одновременно) в которые входит
пользователь или его друзья.:
	Отправляем:
	POST запрос http://127.0.0.1:5000/searchrecord
	в body данные:
	{
    "phone": "+79000000000",
    "password": "пароль" ,
    "word": "слово для поиска"
	}
	Получаем:
	Словарь {id группы: название группы) или 404
Поиск может осуществляться долго, АПИ вк дает только 5 запросов в секунду, предпринята небольшая попытка асинхронно ускорить обработку.

Метод 2) Аналогичен методу 1 (но не учитываем группы друзей), результат поиска сохраняется в БД.
	Отправляем: 
	POST запрос http://127.0.0.1:5000/searchsaverecord
	в body данные:
	{
    "phone": "+79000000000",
    "password": "пароль" ,
    "word": "слово для поиска"
	}
	Получаем:
	Словарь {id группы: название группы) или 404

Метод 3) Возвращает все когда-либо найденные с использованием метода 2 группы (сообщества).
Информация возвращается из БД.
	Отправляем:
	GET http://127.0.0.1:5000/getallrecords
	получаем список групп из БД

Также во время работы с АПИ может возникнуть ошибка капчи. Любой запрос в таком случае должен сделать редирект на http://127.0.0.1:5000/captcha.
Редирект идет через GET запрос с указанием параметров phone=телефон, password=пароль. В ответ получаем словарь, где указан url для решения капчи, и ее SID.
Нужно перейти по урл, записать ответ с капчи в body и отправить POST запрос на этот же адрес. 
POST запрос на адрес http://127.0.0.1:5000/captcha
Пример body: 
{
    "phone": "+79000000000",
    "password": "password": ,
    "word": "word": 
    "sid": [
        12345678
    ],
    "key": "hj76kO"
}
В ответ возвращается строка.

Архив дампа базы данных - dump.sql

## Очистка Docker пространства:
	
    make clear-data