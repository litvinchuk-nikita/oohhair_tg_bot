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
        text='Слабый', callback_data='light')
    middle_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Средний', callback_data='middle')
    strong_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Сильный', callback_data='strong')
    blonde_button: InlineKeyboardButton = InlineKeyboardButton(
        text='Составы для блонда', callback_data='blond')
    kb_builder_blond: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder_blond.add(light_button, middle_button,
                         strong_button, blonde_button)
    kb_builder_blond.adjust(3, 1)
    return kb_builder_blond.as_markup()
