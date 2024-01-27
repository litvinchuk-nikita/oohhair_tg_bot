from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON


def create_pagination_keyboard(pag, url, text_but) -> InlineKeyboardMarkup:
    url_button: InlineKeyboardButton = InlineKeyboardButton(
        text=text_but, url=url)
    forward_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON['forward'], callback_data='forward')
    backward_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON['backward'], callback_data='backward')
    pag_button: InlineKeyboardButton = InlineKeyboardButton(
        text=pag, callback_data='pag')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(url_button, backward_button,
                   pag_button, forward_button)
    kb_builder.adjust(1, 3)
    return kb_builder.as_markup()


def create_pagination_keyboard_practice(pag, url, text_but) -> InlineKeyboardMarkup:
    url_button: InlineKeyboardButton = InlineKeyboardButton(
        text=text_but, url=url)
    forward_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON['forward'], callback_data='forward_pr')
    backward_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON['backward'], callback_data='backward_pr')
    pag_button: InlineKeyboardButton = InlineKeyboardButton(
        text=pag, callback_data='pag')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(url_button, backward_button,
                   pag_button, forward_button)
    kb_builder.adjust(1, 3)
    return kb_builder.as_markup()


def create_pagination_keyboard_promotion(pag, url, text_but) -> InlineKeyboardMarkup:
    url_button: InlineKeyboardButton = InlineKeyboardButton(
        text=text_but, url=url)
    forward_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON['forward'], callback_data='forward_prom')
    backward_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON['backward'], callback_data='backward_prom')
    pag_button: InlineKeyboardButton = InlineKeyboardButton(
        text=pag, callback_data='pag')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(url_button, backward_button,
                   pag_button, forward_button)
    kb_builder.adjust(1, 3)
    return kb_builder.as_markup()