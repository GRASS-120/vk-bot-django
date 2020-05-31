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
        return HttpResponse("771a5e5c")

    # Обработчик сообщений
    if body["type"] == "message_new":

        user_id = body["object"]["message"]["from_id"]
        split_body = body["object"]["message"]["text"].split(maxsplit=3)
        query_msg = database.get("answer", "msg")
        query_group = database.get("groups", "group_name")
        user_msg = body["object"]["message"]["text"]

        if "payload" in body["object"]["message"]:
            payload = body["object"]["message"]["payload"]

            if payload == """{"command":"start"}""":
                keyboard_start(request, user_id)
        
            try:

                if payload == """{"command":"sempai"}""":
                    database.insert_into_users(user_id, 1)
                    msg = f"Отлично, теперь вы {query_group[0][0]}! ⛩️"
                    attachment = f"photo{owner_id}_457239021"
                    send_message(user_id, msg, attachment)

                elif payload == """{"command":"moder"}""":
                    database.insert_into_users(user_id, 2)
                    msg = f"Отлично, теперь вы {query_group[1][0]}! 🛡️"
                    attachment = f"photo{owner_id}_457239020"
                    send_message(user_id, msg, attachment)

                elif payload == """{"command":"user"}""":
                    database.insert_into_users(user_id, 3)
                    msg = f"Отлично, теперь вы {query_group[2][0]}! ♟️"
                    attachment = f"photo{owner_id}_457239022"
                    send_message(user_id, msg, attachment)

            # Если пользователь уже есть в db
            except sqlite3.IntegrityError:
                msg = "Вы уже состоите в группе пользователей! 💢"
                send_message(user_id, msg)

        elif user_msg in query_msg[0][0] and user_msg == "/list":
            msg = database.get("answer")
            print(query_msg[1])
            send_message(user_id, msg)

        elif user_msg in query_msg[2][0] and user_msg == "/start":
            msg = database.get("answer", "answ")[0]
            send_message(user_id, msg)

        # elif user_msg in query_msg[4][0] and user_msg == 'привет':
        #     # hello_text = f'Ну привет-привет, {get_user_name(user_id)}'
        #     # msg = database.update("answer", "answ", hello_text, 5)[0]
        #     msg = "Ну привет-привет"
        #     send_message(user_id, msg) 

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

        elif user_msg == "/change_group":
            user_list = database.get("users")
            # if user_id in user_id_list:
                #удалить пользователя из базы
                #вызвать клаву
                #обработать запрос
            
            database.delete_user(user_id)
            keyboard_start(request, user_id)

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

        # elif "attachments" in body["object"]["message"]:
        #     if body["object"]["message"]["attachments"][0]["type"] == "sticker":
        #         msg = 'Че стикеры шлешь?! 😡'
        #         send_message(user_id, msg)

        # else:
        #     msg = 'Чет не понимаю, что ты мне пишешь, но ты можешь обучить меня с помощью команды /teach'
        #     send_message(user_id, msg)

    return HttpResponse("ok")

#=========== dev =============#

# клавиатура при начале диалога с ботом,
# выбор группы пользоватеcля
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

lg = {
    "success": False,
    "groups": []
}

# рассылка сообщений определенным группам пользователей
def login(request):
    global lg
    tmp = []

    for i in database.get("groups"):
        tmp.append(i)
        print(i)
        print(tmp)

    lg["groups"] = tmp

    if ("login" and "password") in request.GET:
        if "admin" == request.GET.get("login") and "0000" == request.GET.get("password"):
            lg["success"] = True

    elif ("groups" and "message") in request.GET:
        msg = request.GET.get("message")
        users_list = database.get("users")
        group_name = request.GET.get("groups")

        if group_name == 'Sempai':
            for i in range(len(users_list)):
                if lg["groups"][0][0] == users_list[i][1]:
                    send_message(users_list[i][0], msg)

        elif group_name == 'Moder':
            for i in range(len(users_list)):
                if lg["groups"][1][0] == users_list[i][1]:
                    send_message(users_list[i][0], msg)

        elif group_name == "User":
            for i in range(len(users_list)):
                if lg["groups"][2][0] == users_list[i][1]:
                    send_message(users_list[i][0], msg)

    return render(request, "login.html", lg)

