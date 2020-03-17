import vk_api
import requests
import time
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from parsing import gismeteo_parse, headers, base_url, base_url_tomorrow, config_temp
from images import main as imagesDraw
import config_image as conf
import pickle
import random


def send_picture():
    data = vk.photos.getMessagesUploadServer(user_id=event.user_id)
    upload_url = data["upload_url"]
    print('1')
    files = {'photo': open("", 'rb')}
    response = requests.post(upload_url, files=files)
    print('2')
    result = json.loads(response.text)
    uploadResult = vk.photos.saveMessagesPhoto(server=result["server"],
                                                  photo=result["photo"],
                                                  hash=result["hash"])
    print('3')
    vk.messages.send(user_id=event.user_id,
                        message="Погода в Челябинске",
                        attachment='photo{}_{}'.format(uploadResult[0]["owner_id"],
                            uploadResult[0]["id"]))
    print('4')

# основной блок инициализации бота в вк
try:
    time.perf_counter()
    vk_session = vk_api.VkApi(token="")
    time.sleep(random.randint(1, 3))
    vk = vk_session.get_api()
    time.sleep(random.randint(1, 3))
    longpoll = VkLongPoll(vk_session, wait=25)
    time.sleep(random.randint(1, 3))
    vk = vk_session.get_api()
except:
    print('Стартую, с момента ЗАПУСКА прошло - {}'.format(time.perf_counter()))
    time.sleep(random.randint(1, 15))
    longpoll = VkLongPoll(vk_session, wait=25)
    time.sleep(1)
    vk = vk_session.get_api()

print('Запуск..')

# переменная колличества While True циклов
count_while_true = 0

while True:
    try:
        count_while_true += 1
        print('СЛУШАЮ ЧАТ..')
        for event in longpoll.listen():
            print('СЛУШАЮ ЧАТ в longpoll.listen()..')
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.text.lower() == 'погода' or event.text.lower() == 'сделай погоду' or event.text.lower() == 'погода на сегодня':
                    try:
                        vk.messages.send(user_id=event.user_id, random_id=1245780, message='Сейчас будет сделано, подожди..')
                        print('Запускаю парсер на сегодня')
                        gismeteo_parse(base_url, headers)
                        print('Парсер отработал на сегодня')

                        print('Рисую картинку на сегодня')
                        imagesDraw()
                        print('Картинка нарисована на сегодня')

                        print('Отправляю фото на сегодня')
                        send_picture()
                        print('Отправил фото на сегодня')

                        print('С момента запуска прошло: {}'.format(time.perf_counter()))

                        break
                    except:
                        print('ОСТАНОВКА, ПРОШЛО ВРЕМЯ: {}'.format(time.perf_counter()))
                        time.sleep(random.randint(1, 15))
                        longpoll = VkLongPoll(vk_session, wait=25)
                        time.sleep(random.randint(1, 2))
                        vk = vk_session.get_api()
                        print('Сработало исключение на vk.messages.send')
                        while True:
                            try:
                                vk.messages.send(user_id=event.user_id, message='Произошла какая-то ошибка подключения к vk.Api, нужно повторить запрос через 10-15 секунд.')
                                break

                            except:
                                print('ОСТАНОВКА, ПРОШЛО ВРЕМЯ: {}'.format(time.perf_counter()))
                                time.sleep(random.randint(1, 15))
                                longpoll = VkLongPoll(vk_session, wait=25)
                                time.sleep(random.randint(1, 2))
                                vk = vk_session.get_api()
                                print('Сработало исключение WHILE на vk.messages.send')
                        break


                if event.text.lower() == 'погода на завтра' or event.text.lower() == 'сделай погоду на завтра': #Если написали заданную фразу
                    # if event.from_user: #Если написали в ЛС
                    try:
                        vk.messages.send(user_id=event.user_id, message='Сейчас нарисую, жди...')
                        print('Запускаю парсер на завтра')
                        gismeteo_parse(base_url_tomorrow, headers)
                        print('Парсер отработал на завтра')

                        print('Рисую картинку на завтра')
                        imagesDraw()
                        print('Картинка нарисована на завтра')

                        print('Отправляю фото на завтра')
                        send_picture()
                        print('Отправил фото на завтра')
                        print('С момента запуска прошло: {}'.format(time.perf_counter()))

                        break
                    except:
                        print('ОСТАНОВКА, ПРОШЛО ВРЕМЯ: {}'.format(time.perf_counter()))
                        time.sleep(random.randint(1, 15))
                        longpoll = VkLongPoll(vk_session, wait=25)
                        time.sleep(random.randint(1, 2))
                        vk = vk_session.get_api()
                        print('Сработало исключение на vk.messages.send')
                        while True:
                            try:
                                vk.messages.send(user_id=event.user_id, message='Произошла какая-то ошибка подключения к vk.Api, нужно повторить запрос через 10-15 секунд.')
                                break

                            except:
                                print('ОСТАНОВКА, ПРОШЛО ВРЕМЯ: {}'.format(time.perf_counter()))
                                time.sleep(random.randint(1, 15))
                                longpoll = VkLongPoll(vk_session, wait=25)
                                time.sleep(random.randint(1, 2))
                                vk = vk_session.get_api()
                                print('Сработало исключение WHILE на vk.messages.send')
                        break

    # except requests.exceptions.ConnectionResetError:
    #     longpoll = VkLongPoll(vk_session, wait=25)
    #     vk = vk_session.get_api()
    #     print('Сработало исключение ConnectionResetError, пытаюсь переподключится!')

    # except requests.exceptions.ConnectionError:
    #     longpoll = VkLongPoll(vk_session, wait=25)
    #     vk = vk_session.get_api()
    #     print('Сработало исключение ConnectionError, пытаюсь переподключится!')

    except:
        print('ОСТАНОВКА, ПРОШЛО ВРЕМЯ: {}'.format(time.perf_counter()))
        time.sleep(random.randint(1, 15))
        longpoll = VkLongPoll(vk_session, wait=25)
        time.sleep(random.randint(1, 2))
        vk = vk_session.get_api()
        print('Сработало исключение на VkLongPoll,  пытаюсь переподключится!')

    time.sleep(random.randint(1, 15))
    print('Итерация цикла While True № - {}.'.format(count_while_true))

