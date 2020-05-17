from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import json
import vk
import random
import sqlite3
import database

secret_key = "very1secre2tkey3vk4bota"
session = vk.Session(access_token="93b63503f60a88bd1efa8a9b051188ef3bd0f99ac5496e3d038f0e0a935716012c6aff2994437a11d18f0")
vkAPI = vk.API(session)

# Функция-обработчик
@csrf_exempt
def bot(request):
    body = json.loads(request.body)
    owner_id = -194135879
    print(body)

    # Подтверждение сервера
    if body == {"type": "confirmation", "group_id": 194135879, "secret": "very1secre2tkey3vk4bota"}:  #Берем запрос и ответ в CallBack API 
        return HttpResponse("2e6cbf64")

    if body["type"] == "message_new":

        user_id = body["object"]["message"]["from_id"]
        split_body = body["object"]["message"]["text"].split(maxsplit=3)
        query_msg = database.get("answer", "msg")
        user_msg = body["object"]["message"]["text"]

        if user_msg == 'Начать':
            if body["object"]["message"]["payload"] == """{"command":"start"}""":
                keyboard_start(request, user_id)

        elif user_msg in query_msg[0][0] and user_msg == "/list":
            msg = database.get("answer")
            print(query_msg[1])
            send_message(user_id, msg)

        elif user_msg in query_msg[2][0] and user_msg == "/start":
            msg = database.get("answer", "answ")[0]
            send_message(user_id, msg)

        elif user_msg.casefold() in query_msg[4][0] and user_msg.casefold() == 'привет':
            hello_text = f'Ну привет-привет, {get_user_name(user_id)}'
            msg = database.update("answer", "answ", hello_text, 5)[0]
            send_message(user_id, msg) 

        elif split_body[0] == '/say':
            if len(split_body) == 2:
                text = split_body[1]
            elif len(split_body) == 3:
                text = f"{split_body[1]} {split_body[2]}"
            else:
                text = f"{split_body[1]} {split_body[2]} {split_body[3]}"
            msg = text
            send_message(user_id, msg)

        elif user_msg in query_msg[1][0] and user_msg == "/post":
            msg = database.get("answer", "answ")[2]
            attachment = f"wall{owner_id}_2"
            send_message(user_id, msg, attachment)

        elif split_body[0] == '/teach':
            if len(split_body) == 4:
                db_msg = split_body[1]
                db_answ = split_body[2]

                database.insert_into("answer", db_msg, db_answ)
                msg = database.get("answer", "answ")[3]
                send_message(user_id, msg)
            else:
                msg = "При обучении бота что-то пошло не так. Проверь правильность написания команды"
                send_message(user_id, msg)

        # elif body["object"]["message"]["attachments"][0]["type"] == "sticker":
        #     msg = 'Че стикеры шлешь?! 😡'
        #     send_message(user_id, msg)
        #     print(body)

        else:
            msg = 'Чет не понимаю, что ты мне пишешь, но ты можешь обучить меня с помощью команды /teach'
            send_message(user_id, msg)

    return HttpResponse("ok")

########

def keyboard_start(request, user_id):
    msg = "Привет! Выбери свою группу пользователя:"
    keyboard = json.dumps({
        "one_time": True,
        "buttons": [[
            {
                "action": {
                    "type": "text",
                    "label": "Sempai",
                    "payload": """{"command": "sempai"}"""
                },
                "color": "negative"
            },
            {
                "action": {
                    "type": "text",
                    "label": "Moder",
                    "payload": """{"command": "moder"}"""
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "User",
                    "payload": """{"command": "user"}"""
                },
                "color": "positive"
            }
        ]]
    })

    send_message(user_id, msg, keyboard = keyboard)

# Получение имени пользователя
def get_user_name(user_id):
    return vkAPI.users.get(user_id=user_id, v=5.103)[0]['first_name']

# Получения города пользоваеля 
def get_user_city(user_id):
    return vkAPI.users.get(user_id=user_id, fields='city', v=5.103)[0]['city']['title']

# Отправка сообщения
def send_message(user_id="", msg="", attachment="", keyboard=""):
    vkAPI.messages.send(user_id=user_id, message=msg, keyboard=keyboard, random_id=random.randint(1, 999999999999999999), attachment=attachment, v=5.103)

         

