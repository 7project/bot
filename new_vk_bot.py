import vk_api
import requests
import time
from vk_api.longpoll import VkLongPoll, VkEventType
import json
from parsing import gismeteo_parse, headers, base_url, config_temp
from images import main as imagesDraw
import config_image as conf
import pickle


vk_session = vk_api.VkApi(token="")
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
    # and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:
        if event.text.lower() == 'погода' or event.text.lower() == 'сделай погоду': #Если написали заданную фразу
            # if event.from_user: #Если написали в ЛС
            vk.messages.send(user_id=event.user_id, message='Сейчас нарисую, жди...')
            print('Запускаю парсер')
            gismeteo_parse(base_url, headers)
            print('Парсер отработал')

            print('Рисую картинку')
            imagesDraw()
            print('Картинка нарисована')

            print('Отправляю фото')
            data = vk.photos.getMessagesUploadServer(user_id=event.user_id)
            upload_url = data["upload_url"]
            files = {'photo': open("", 'rb')}
            response = requests.post(upload_url, files=files)
            result = json.loads(response.text)
            uploadResult = vk.photos.saveMessagesPhoto(server=result["server"],
                                                          photo=result["photo"],
                                                          hash=result["hash"])
            vk.messages.send(user_id=event.user_id,
                                message="Погода в Челябинске",
                                attachment='photo{}_{}'.format(uploadResult[0]["owner_id"],
                                    uploadResult[0]["id"]))
            print('Отправил фото')
            print(uploadResult)