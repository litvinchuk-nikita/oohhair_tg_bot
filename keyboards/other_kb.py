from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_polirovka_kb(url) -> InlineKeyboardMarkup:
    url_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Запись урока', url=url)
    kb_builder_pol: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_pol.add(url_button)
    return kb_builder_pol.as_markup()


def create_notion_kb(url_android, url_ios) -> InlineKeyboardMarkup:
    url_button_android: InlineKeyboardButton = InlineKeyboardButton(
        text='Для Android', url=url_android)
    url_button_ios: InlineKeyboardButton = InlineKeyboardButton(
        text='Для IOS', url=url_ios)
    kb_builder_notion: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_notion.add(url_button_android, url_button_ios)
    return kb_builder_notion.as_markup()


def create_smm_kb(url) -> InlineKeyboardMarkup:
    url_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Основы СММ', url=url)
    kb_builder_smm: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_smm.add(url_button)
    return kb_builder_smm.as_markup()


def create_yesno_kb() -> InlineKeyboardMarkup:
    yes_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Да', callback_data='yes')
    no_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Нет', callback_data='no')
    kb_builder_yesno: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_yesno.add(yes_button, no_button)
    return kb_builder_yesno.as_markup()


def create_presentation_kb(url) -> InlineKeyboardMarkup:
    url_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Скачать презентацию', url=url)
    kb_builder_pres: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_pres.add(url_button)
    return kb_builder_pres.as_markup()


def create_memo_kb() -> InlineKeyboardMarkup:
    light_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Легкие', callback_data='light')
    lightmiddle_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Легкие - средние', callback_data='lightmiddle')
    middle_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Средние', callback_data='middle')
    middlestrong_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Средние - сильные', callback_data='middlestrong')
    strong_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Сильные', callback_data='strong')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(light_button, lightmiddle_button, middle_button,
                         middlestrong_button, strong_button)
    kb_builder.adjust(1, 1, 1, 1, 1)
    return kb_builder.as_markup()


def create_injury_kb() -> InlineKeyboardMarkup:
    button_1: InlineKeyboardButton = InlineKeyboardButton(
        text='1/2 степень тонкие', callback_data='1/2 thin')
    button_2: InlineKeyboardButton = InlineKeyboardButton(
        text='1/2 степень средние', callback_data='1/2 middle')
    button_3: InlineKeyboardButton = InlineKeyboardButton(
        text='1/2 степень толстые', callback_data='1/2 fat')
    button_4: InlineKeyboardButton = InlineKeyboardButton(
        text='3/4 степень тонкие', callback_data='3/4 thin')
    button_5: InlineKeyboardButton = InlineKeyboardButton(
        text='3/4 степень средние', callback_data='3/4 middle')
    button_6: InlineKeyboardButton = InlineKeyboardButton(
        text='3/4 степень толстые', callback_data='3/4 fat')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(button_1, button_2, button_3, button_4, button_5, button_6)
    kb_builder.adjust(1, 1, 1, 1, 1, 1)
    return kb_builder.as_markup()
