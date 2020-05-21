import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token='token')

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:
            if event.text == "Начать":
                #Создаем меню с кнопками
                keyboard = VkKeyboard(one_time=True)
                #Добавляем кнопку
                keyboard.add_button("Кнопка 1", color=VkKeyboardColor.PRIMARY)
                keyboard.add_button("Кнопка 2", color=VkKeyboardColor.PRIMARY)

                #Перенос на новую строку
                keyboard.add_line()
                keyboard.add_button("Новая Кнопка 1", color=VkKeyboardColor.PRIMARY)
                keyboard.add_button("Новая Кнопка 2", color=VkKeyboardColor.PRIMARY)

                vk.messages.send(
                    user_id=event.user_id,
                    message="Сообщение",
                    random_id=random.randint(1, 2147483647),
                    keyboard=keyboard.get_keyboard() #Эта строчка добавляет кнопки
                )