from copy import deepcopy
import requests
from config_data.config import Config, load_config
from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message
from filters.filters import IsAdmin, AddUserTheory, AddUserPractice, AddUserPolirovka, AddUserSMM, AddUserPromotion
from database.database import (users_db, user_dict_template_theory, users_db_pr, user_dict_template_practice, insert_theory, select_theory_id,
                              insert_practice, select_practice_id, insert_polirovka, select_polirovka_id, insert_smm, select_smm_id,
                              select_promotion_id, insert_promotion, user_dict_template_promotion, users_db_prom)
from keyboards.pagination_kb import create_pagination_keyboard, create_pagination_keyboard_practice, create_pagination_keyboard_promotion
from keyboards.other_kb import create_polirovka_kb, create_notion_kb, create_smm_kb, create_yesno_kb, create_presentation_kb, create_memo_kb, create_injury_kb
from lexicon.lexicon import LEXICON, LEXICON_LESSONS_NAME, LEXICON_LESSONS_URL, LEXICON_LESSONS_PRACTICE, LEXICON_LESSONS_PRACTICE_URL, LEXICON_LESSONS_PROMOTION, LEXICON_LESSONS_PROMOTION_URL

router: Router = Router()


# загружаем конфиг в переменную config
config: Config = load_config()


# этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart())
async def process_start_cammand(message: Message):
    theory_id_list = select_theory_id()
    if message.from_user.id in theory_id_list:
        await message.answer(LEXICON['open'])
    else:
        await message.answer(LEXICON['/start'])
        params: dict[str, str] = {
            'chat_id': f'{config.tg_bot.admin_ids[0]}',
            'text': f'Пользователь {message.from_user.full_name} запрашивает доступ к обучению. '
            f'ID: {message.from_user.id}\ntg: @{message.from_user.username}'}
        response = requests.get(
            'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)
        params: dict[str, str] = {
            'chat_id': f'{config.tg_bot.admin_ids[1]}',
            'text': f'Пользователь {message.from_user.full_name} запрашивает доступ к обучению. '
            f'ID: {message.from_user.id}\ntg: @{message.from_user.username}'}
        response = requests.get(
            'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)


# этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])


# этот хэндлер будет срабатывать на команду "/teory"
# и отправлять пользователю первый теоритический урок с кнопками пагинации
@router.message(Command(commands='theory'))
async def process_teory_command(message: Message):
    theory_id_list = select_theory_id()
    if message.from_user.id in theory_id_list:
        if message.from_user.id not in users_db:
            users_db[message.from_user.id] = deepcopy(user_dict_template_theory)
        text_but = LEXICON_LESSONS_NAME[str(
            users_db[message.from_user.id]['less'])]
        text = LEXICON['/theory']
        url = LEXICON_LESSONS_URL[str(users_db[message.from_user.id]['less'])]
        pag = f'{users_db[message.from_user.id]["less"]}/{len(LEXICON_LESSONS_NAME)}'
        await message.answer(
            text=text,
            reply_markup=create_pagination_keyboard(pag, url, text_but))
        await message.answer(LEXICON['presentation'], reply_markup=create_yesno_kb())
    else:
        await message.answer(LEXICON['close'])


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком уроков теории
@router.callback_query(Text(text='forward'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['less'] < 24:
        users_db[callback.from_user.id]['less'] += 1
    elif users_db[callback.from_user.id]['less'] == 24:
        users_db[callback.from_user.id]['less'] = 1
    text_but = LEXICON_LESSONS_NAME[str(
        users_db[callback.from_user.id]['less'])]
    text = LEXICON['/theory']
    url = LEXICON_LESSONS_URL[str(users_db[callback.from_user.id]['less'])]
    pag = f'{users_db[callback.from_user.id]["less"]}/{len(LEXICON_LESSONS_NAME)}'
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard(pag, url, text_but))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком уроков теории
@router.callback_query(Text(text='backward'))
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['less'] > 1:
        users_db[callback.from_user.id]['less'] -= 1
    elif users_db[callback.from_user.id]['less'] == 1:
        users_db[callback.from_user.id]['less'] = 24
    text_but = LEXICON_LESSONS_NAME[str(
        users_db[callback.from_user.id]['less'])]
    text = LEXICON['/theory']
    url = LEXICON_LESSONS_URL[str(users_db[callback.from_user.id]['less'])]
    pag = f'{users_db[callback.from_user.id]["less"]}/{len(LEXICON_LESSONS_NAME)}'
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard(pag, url, text_but))
    await callback.answer()


# этот хэндлер будет срабатывать на команду "/polirovka"
# и отправлять пользователю урок по полировке волос
@router.message(Command(commands='polirovka'))
async def process_polirovka_command(message: Message):
    users_id_polir = select_polirovka_id()
    if message.from_user.id in users_id_polir:
        url_pol = LEXICON_LESSONS_URL['pol']
        text_pol = LEXICON['polirovka']
        await message.answer(
            text=text_pol,
            reply_markup=create_polirovka_kb(url_pol))
    else:
        await message.answer(LEXICON['close'])


# этот хэндлер будет срабатывать на команду "/smm"
# и отправлять пользователю ссылку на курс по смм
@router.message(Command(commands='smm'))
async def process_smm_command(message: Message):
    users_id_smm = select_smm_id()
    if message.from_user.id in users_id_smm:
        text_notion = LEXICON['notion']
        url_android = LEXICON_LESSONS_URL['android']
        url_ios = LEXICON_LESSONS_URL['ios']
        await message.answer(
            text=text_notion,
            reply_markup=create_notion_kb(url_android, url_ios))
        url_smm = LEXICON_LESSONS_URL['smm']
        await message.answer(
            text=LEXICON['smm'],
            reply_markup=create_smm_kb(url_smm))
    else:
        await message.answer(LEXICON['close'])


# этот хэндлер будет срабатывать на команду "/practice"
# и отправлять пользователю первый практический урок с кнопками пагинации
@router.message(Command(commands='practice'))
async def process_practice_command(message: Message):
    users_id_pr = select_practice_id()
    if message.from_user.id in users_id_pr:
        if message.from_user.id not in users_db_pr:
            users_db_pr[message.from_user.id] = deepcopy(user_dict_template_practice)
        text_but = LEXICON_LESSONS_PRACTICE[str(
            users_db_pr[message.from_user.id]['practice'])]
        text = LEXICON['/practice']
        url = LEXICON_LESSONS_PRACTICE_URL[str(
            users_db_pr[message.from_user.id]['practice'])]
        pag = f'{users_db_pr[message.from_user.id]["practice"]}/{len(LEXICON_LESSONS_PRACTICE)}'
        await message.answer(
            text=text,
            reply_markup=create_pagination_keyboard_practice(pag, url, text_but))
        await message.answer(LEXICON['final'])
    else:
        await message.answer(LEXICON['close'])


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком уроков практики
@router.callback_query(Text(text='forward_pr'))
async def process_forward_press(callback: CallbackQuery):
    if users_db_pr[callback.from_user.id]['practice'] < 2:
        users_db_pr[callback.from_user.id]['practice'] += 1
    elif users_db_pr[callback.from_user.id]['practice'] == 2:
        users_db_pr[callback.from_user.id]['practice'] = 1
    text_but = LEXICON_LESSONS_PRACTICE[str(
        users_db_pr[callback.from_user.id]['practice'])]
    text = LEXICON['/practice']
    url = LEXICON_LESSONS_PRACTICE_URL[str(
        users_db_pr[callback.from_user.id]['practice'])]
    pag = f'{users_db_pr[callback.from_user.id]["practice"]}/{len(LEXICON_LESSONS_PRACTICE)}'
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard_practice(pag, url, text_but))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком уроков практики
@router.callback_query(Text(text='backward_pr'))
async def process_backward_press(callback: CallbackQuery):
    if users_db_pr[callback.from_user.id]['practice'] > 1:
        users_db_pr[callback.from_user.id]['practice'] -= 1
    elif users_db_pr[callback.from_user.id]['practice'] == 1:
        users_db_pr[callback.from_user.id]['practice'] = 2
    text_but = LEXICON_LESSONS_PRACTICE[str(
        users_db_pr[callback.from_user.id]['practice'])]
    text = LEXICON['/practice']
    url = LEXICON_LESSONS_PRACTICE_URL[str(
        users_db_pr[callback.from_user.id]['practice'])]
    pag = f'{users_db_pr[callback.from_user.id]["practice"]}/{len(LEXICON_LESSONS_PRACTICE)}'
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard_practice(pag, url, text_but))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "да"
# во время взаимодействия пользователя с сообщением про презентацию
@router.callback_query(Text(text='yes'))
async def process_yes_press(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки пагинации
# во время взаимодействия пользователя со списком уроков
@router.callback_query(Text(text='pag'))
async def process_pag_press(callback: CallbackQuery):
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "нет"
# во время взаимодействия пользователя с сообщением про презентацию
@router.callback_query(Text(text='no'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON['no']
    url = LEXICON_LESSONS_URL['presentation']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_presentation_kb(url))
    await callback.answer()


# этот хэндлер будет срабатывать на команду "/memo"
# и отправлять пользователю памятку по составам
@router.message(Command(commands='memo'))
async def process_memo_command(message: Message):
    user_id_theory = select_theory_id()
    user_id_prom = select_promotion_id()
    if message.from_user.id in user_id_theory or message.from_user.id in user_id_prom:
        text = LEXICON['/memo']
        await message.answer(
            text=text,
            parse_mode='HTML',
            reply_markup=create_memo_kb())
    else:
        await message.answer(LEXICON['close'])


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Сильные"
# во время взаимодействия пользователя с памяткой по составам
@router.callback_query(Text(text='strong'))
async def process_strong_press(callback: CallbackQuery):
    text = LEXICON['strong']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_memo_kb())
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Средние-сильные"
# во время взаимодействия пользователя с памяткой по составам
@router.callback_query(Text(text='middlestrong'))
async def process_strong_press(callback: CallbackQuery):
    text = LEXICON['middlestrong']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_memo_kb())
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Средние"
# во время взаимодействия пользователя с памяткой по составам
@router.callback_query(Text(text='middle'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON['middle']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_memo_kb())
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Легкие-средние"
# во время взаимодействия пользователя с памяткой по составам
@router.callback_query(Text(text='lightmiddle'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON['lightmiddle']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_memo_kb())
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Легкие"
# во время взаимодействия пользователя с памяткой по составам
@router.callback_query(Text(text='light'))
async def process_backward_press(callback: CallbackQuery):
    text = LEXICON['light']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_memo_kb())
    await callback.answer()


# этот хэндлер будет срабатывать на команду "/reminder"
# и отправлять пользователю памятку по составам
@router.message(Command(commands='reminder'))
async def process_memo_command(message: Message):
    user_id_theory = select_theory_id()
    user_id_prom = select_promotion_id()
    if message.from_user.id in user_id_theory or message.from_user.id in user_id_prom:
        text = LEXICON['injury']
        await message.answer(
            text=text,
            parse_mode='HTML',
            reply_markup=create_injury_kb())
    else:
        await message.answer(LEXICON['close'])


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "1/2 степень тонкие"
# во время взаимодействия пользователя с памяткой по степени повреждения волоса
@router.callback_query(Text(text='1/2 thin'))
async def process_thin_press(callback: CallbackQuery):
    text = LEXICON['1/2 thin']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_injury_kb())
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "1/2 степень средние"
# во время взаимодействия пользователя с памяткой по степени повреждения волоса
@router.callback_query(Text(text='1/2 middle'))
async def process_thin_press(callback: CallbackQuery):
    text = LEXICON['1/2 middle']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_injury_kb())
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "1/2 степень толстые"
# во время взаимодействия пользователя с памяткой по степени повреждения волоса
@router.callback_query(Text(text='1/2 fat'))
async def process_thin_press(callback: CallbackQuery):
    text = LEXICON['1/2 fat']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_injury_kb())
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "3/4 степень тонкие"
# во время взаимодействия пользователя с памяткой по степени повреждения волоса
@router.callback_query(Text(text='3/4 thin'))
async def process_thin_press(callback: CallbackQuery):
    text = LEXICON['3/4 thin']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_injury_kb())
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "3/4 степень средние"
# во время взаимодействия пользователя с памяткой по степени повреждения волоса
@router.callback_query(Text(text='3/4 middle'))
async def process_thin_press(callback: CallbackQuery):
    text = LEXICON['3/4 middle']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_injury_kb())
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "3/4 степень толстые"
# во время взаимодействия пользователя с памяткой по степени повреждения волоса
@router.callback_query(Text(text='3/4 fat'))
async def process_thin_press(callback: CallbackQuery):
    text = LEXICON['3/4 fat']
    await callback.message.edit_text(
        text=text,
        reply_markup=create_injury_kb())
    await callback.answer()


# этот хэндлер будет срабатывать на команду "/promotion"
# и отправлять пользователю первый урок повышения с кнопками пагинации
@router.message(Command(commands='promotion'))
async def process_promotion_command(message: Message):
    users_id_prom = select_promotion_id()
    if message.from_user.id in users_id_prom:
        if message.from_user.id not in users_db_prom:
            users_db_prom[message.from_user.id] = deepcopy(user_dict_template_promotion)
        text_but = LEXICON_LESSONS_PROMOTION[str(
            users_db_prom[message.from_user.id]['promotion'])]
        text = LEXICON['/promotion']
        url = LEXICON_LESSONS_PROMOTION_URL[str(
            users_db_prom[message.from_user.id]['promotion'])]
        pag = f'{users_db_prom[message.from_user.id]["promotion"]}/{len(LEXICON_LESSONS_PROMOTION)}'
        await message.answer(
            text=text,
            reply_markup=create_pagination_keyboard_promotion(pag, url, text_but))
        await message.answer(LEXICON['presentation'], reply_markup=create_yesno_kb())
    else:
        await message.answer(LEXICON['close'])


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя со списком уроков для повышения
@router.callback_query(Text(text='forward_prom'))
async def process_forward_press(callback: CallbackQuery):
    if users_db_prom[callback.from_user.id]['promotion'] < len(LEXICON_LESSONS_PROMOTION):
        users_db_prom[callback.from_user.id]['promotion'] += 1
    elif users_db_prom[callback.from_user.id]['promotion'] == len(LEXICON_LESSONS_PROMOTION):
        users_db_prom[callback.from_user.id]['promotion'] = 1
    text_but = LEXICON_LESSONS_PROMOTION[str(
        users_db_prom[callback.from_user.id]['promotion'])]
    text = LEXICON['/promotion']
    url = LEXICON_LESSONS_PROMOTION_URL[str(
        users_db_prom[callback.from_user.id]['promotion'])]
    pag = f'{users_db_prom[callback.from_user.id]["promotion"]}/{len(LEXICON_LESSONS_PROMOTION)}'
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard_promotion(pag, url, text_but))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя со списком уроков для повышения
@router.callback_query(Text(text='backward_prom'))
async def process_backward_press(callback: CallbackQuery):
    if users_db_prom[callback.from_user.id]['promotion'] > 1:
        users_db_prom[callback.from_user.id]['promotion'] -= 1
    elif users_db_prom[callback.from_user.id]['promotion'] == 1:
        users_db_prom[callback.from_user.id]['promotion'] = len(LEXICON_LESSONS_PROMOTION)
    text_but = LEXICON_LESSONS_PROMOTION[str(
        users_db_prom[callback.from_user.id]['promotion'])]
    text = LEXICON['/promotion']
    url = LEXICON_LESSONS_PROMOTION_URL[str(
        users_db_prom[callback.from_user.id]['promotion'])]
    pag = f'{users_db_prom[callback.from_user.id]["promotion"]}/{len(LEXICON_LESSONS_PROMOTION)}'
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard_promotion(pag, url, text_but))
    await callback.answer()


# этот хэндлер будет срабатывать на отправку id пользователя
# и открывать ему доступ к теории
@router.message(IsAdmin(config.tg_bot.admin_ids), AddUserTheory())
async def add_user(message: Message):
    insert_theory(message.text)
    await message.answer('Пользователь добавлен')
    params = {
        'chat_id': int(message.text),
        'text': f'{LEXICON["open_th"]}'}
    response = requests.get(
        'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)


# этот хэндлер будет срабатывать на отправку id пользователя
# и открывать ему доступ к практике
@router.message(IsAdmin(config.tg_bot.admin_ids), AddUserPractice())
async def add_user(message: Message):
    insert_practice(int((message.text).split('_')[0]))
    await message.answer('Пользователь добавлен')
    params = {
        'chat_id': int((message.text).split('_')[0]),
        'text': f'{LEXICON["open_pr"]}'}
    response = requests.get(
        'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)


# этот хэндлер будет срабатывать на отправку id пользователя
# и открывать ему доступ к полировке
@router.message(IsAdmin(config.tg_bot.admin_ids), AddUserPolirovka())
async def add_user(message: Message):
    insert_polirovka(int((message.text).split('_')[0]))
    await message.answer('Пользователь добавлен')
    params = {
        'chat_id': int((message.text).split('_')[0]),
        'text': f'{LEXICON["open_polir"]}'}
    response = requests.get(
        'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)


# этот хэндлер будет срабатывать на отправку id пользователя
# и открывать ему доступ к smm
@router.message(IsAdmin(config.tg_bot.admin_ids), AddUserSMM())
async def add_user(message: Message):
    insert_smm(int((message.text).split('_')[0]))
    await message.answer('Пользователь добавлен')
    params = {
        'chat_id': int((message.text).split('_')[0]),
        'text': f'{LEXICON["open_smm"]}'}
    response = requests.get(
        'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)


# этот хэндлер будет срабатывать на отправку id пользователя
# и открывать ему доступ к повышению
@router.message(IsAdmin(config.tg_bot.admin_ids), AddUserPromotion())
async def add_user(message: Message):
    insert_promotion(int((message.text).split('_')[0]))
    await message.answer('Пользователь добавлен')
    params = {
        'chat_id': int((message.text).split('_')[0]),
        'text': f'{LEXICON["open_prom"]}'}
    response = requests.get(
        'https://api.telegram.org/bot' + config.tg_bot.token + '/sendMessage', params=params)