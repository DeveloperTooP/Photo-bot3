import telebot
from config import TOKEN, path
import os
from datetime import datetime
from pathlib import Path
from photo_edit import pedit


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sti = open('D:/Python/Photo_Bot-2/stik/stik.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы отправлять тебе картики с текстом в ответ, отправь мне любую картинку🖼".format(message.from_user, bot.get_me()),
        parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    sti = open('D:/Python/Photo_Bot-2/stik/stik1.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Подожди секунду⏳".format(message.from_user, bot.get_me()), 
        parse_mode='html')
    file_photo = bot.get_file(message.photo[-1].file_id)  # Забираем ID фото
    filename, file_extension = os.path.splitext(file_photo.file_path)  # Берем имя файла и расширение
    downloaded_photo = bot.download_file(file_photo.file_path)  # скачиваем с телеграмма
    photo_name = str(datetime.now().strftime("%Y-%m-%d_%H_%M_%S")) + "_" + str(message.from_user.id) + file_extension
    src = Path(path, photo_name)
    with open(src, "wb") as new_file:
        new_file.write(downloaded_photo)  # Сохраняем файл на сервере
    bot.send_photo(message.chat.id, pedit(photo_name))  # Редактируем файл и отправляем пользователю
    sti = open('D:/Python/Photo_Bot-2/stik/stik2.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Держи свою картинку с текстом в ответ😉\nСкорее поделись ей".format(message.from_user, bot.get_me()), 
        parse_mode='html')



bot.polling(none_stop=True)
