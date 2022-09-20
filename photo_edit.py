from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from config import path
from collection import txt
import random


def pedit(name):
    text = random.choice(txt)  # Рандомим текст
    file = Image.open(Path(path, name))  # открываем фото (сохраненное)
    font = ImageFont.load_default()  # Подключаем шрифт
    ptext = ImageDraw.Draw(file)
    ptext.text((640, 745), text, font=font, fill='black', size=250)  # Пишем текст
    return file  # Возвращаем готовое фото
