from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import json
import vk
import random
import sqlite3

secret_key = ""
session = vk.Session(access_token="")
vkAPI = vk.API(session)

# Функция-обработчик
@csrf_exempt
def bot(request):
    body = json.loads(request.body)
    random_id = random.randint(1, 999999999999999999)
    owner_id = 

    # Подключение БД
    connect = sqlite3.connect('db.sqlite')
    cur = connect.cursor()

    # print(body)

    # Подтверждение сервера
    if body == {"type": "confirmation", "group_id": , "secret": ""}:  #Берем запрос и ответ в CallBack API 
        return HttpResponse("4d53ecd7")

    if body["type"] == "message_new":

        user_id = body["object"]["message"]["from_id"]
        split_body = body["object"]["message"]["text"].split(maxsplit=1)
        query_msg = cur.execute("SELECT msg FROM answer").fetchall()
        user_msg = body["object"]["message"]["text"]

        if user_msg == "/list":
            query = "SELECT * FROM answer"
            cur.execute(query)
            msg = cur.fetchall()
            send_message(user_id, msg, random_id)

        elif user_msg in query_msg[0] and user_msg == "/start":
            query = "SELECT answ FROM answer"
            cur.execute(query)
            msg = cur.fetchall()[0]
            send_message(user_id, msg, random_id)
            print(query_msg)

        elif user_msg.casefold() == 'привет':
            msg = f"Ну привет-привет, {get_user_name(user_id)} 👋"
            send_message(user_id, msg, random_id) 

        elif split_body[0] == '/say':
            text = split_body[1]
            msg = text
            send_message(user_id, msg, random_id)

        elif user_msg in query_msg[1] and user_msg == "/post":
            query = "SELECT answ FROM answer"
            cur.execute(query)
            msg = cur.fetchall()[1]
            attachment = f"wall{owner_id}_2"
            send_message(user_id, msg, random_id, attachment)

        else:
            msg = 'Чет не понимаю, что ты мне пишешь'
            send_message(user_id, msg, random_id)
            
    # # Стикеры 
    # # if body["type"] == "message_new":
    # #     if body["object"]["message"]["text"] == "":
    # #         if body["object"]["message"]["attachments"][0]["type"] == "sticker":
    # #             user_id = body["object"]["message"]["from_id"]
    # #               msg = 'Че стикеры шлешь?! 😡'
    # #                send_message(user_id, msg, random_id)

    connect.close()
    return HttpResponse("ok")

########

# Получение имени пользователя
def get_user_name(user_id):
    return vkAPI.users.get(user_id=user_id, v=5.103)[0]['first_name']

# Получения города пользоваеля 
def get_user_city(user_id):
    return vkAPI.users.get(user_id=user_id, fields='city', v=5.103)[0]['city']['title']

# Отправка сообщения
def send_message(user_id, msg, random_id, attachment=""):
    vkAPI.messages.send(user_id=user_id, message=msg, random_id=random_id, attachment=attachment, v=5.103)

         

