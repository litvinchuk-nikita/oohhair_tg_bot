LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': f'Привет!\nЗапрос на открытие доступа к курсу отправлен💌\n'
              'Дай мне несколько минут для одобрения и я открою тебе первые уроки🧠',
    'open_th': f'Доступ к теоритической части курса открыт🤍\nДля ознакомления с функционалом бота введите /help',
    'open_pr': f'Доступ к практической части курса\nоткрыт🤍\nДля ознакомления с функционалом бота введите /help',
    'open_polir': f'Доступ к уроку по полировке волос открыт🤍\nДля ознакомления с функционалом бота введите /help',
    'open_smm': f'Доступ к разделу по СММ открыт🤍\nДля ознакомления с функционалом бота введите /help',
    'open': f'Доступ к курсу открыт🤍\nДля ознакомления с функционалом бота введите /help',
    'close': 'Доступ закрыт',
    '/help': f'Привет, этот бот предназначен для прохождения курса в OOHHAIR SCHOOL\n\n'
             f'Доступные команды:\n/start - Отправить запрос доступа к курсу\n'
             f'/theory - Теоритическая часть\n'
             f'/smm -  Основы СММ\n/practice - Практическая часть\n'
             f'/polirovka - Урок по полировке волос\n'
             f'/memo - Памятка по составам\n'
             f'/help -справка по работе бота\n\nПриятной учебы😊',
    '/theory': f'Бери ручку c тетрадкой и открывай каждый урок по порядку📝\n'
               f'Если нет возможности посмотреть все уроки до нашей первой встречи,'
               f' посмотреть обязательно первых 12✨\nПриятного просмотра🎬',
    'presentation': f'В описании к последнему видео была презентация домашнего ухода,\n'
               f'ты скачала ее?',
    'no': 'Тогда переходи по ссылке, чтобы скачать презентацию😊',
    'polirovka': 'Полировку волос мы подробно изучим на нашей встрече,'
               f'но я решила поделиться записью урока с тобой ♥️\n'
               'Держи!',
    'notion': f'Скачай приложение Notion, зарегистрируйся и напиши мне\nв личные сообщения '
              f'почту, на которую зарегестрировалась☺️\n\n'
              'Ссылки для скачивания приложения:',
    'smm': 'После регистрации переходи по ссылке:',
    '/practice': 'Смотри по очереди😊',
    '/memo': 'Выбери состав по силе выпрямления, который тебе нужен:',
    'strong': f'Сильные:\n1) vier macadamia/definitive\n2) happy hair macadamia\n3) natureze cacao',
    'middle': f'Средние:\n1) happy hair bb\n2) cafe verde natureze\n3) nutrimax\n4) revolution maxwell\n5) zoom organoplastia',
    'light': f'Слабые:\n1) ultimate maxwell\n2) oleo m happy hair\n3) zoom organoplastia blond\n4) prodiva divaplastia',
    'blond': f'Сильные/средние:\n1) nutrimax\n2) bb plastia\n\nСлабые:\n1) oleo m\n2) ultimate maxwell\n3) prodiva divaplastia',
    'other': f'Не понимаю вас..\nДля ознакомления с возможностями бота введите команду /help',
    'final': f'Ура! Поздравляю, теперь ты знаешь все, осталось все освоить на практике.\n'
             'Не стесняйся возвращаться и пересматривать видео несколько раз🫶🏻'}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'Отправить запрос доступа к курсу',
    '/help': 'Справка по работе бота',
    '/theory': 'Теоритическая часть',
    '/smm': 'Основы СММ',
    '/practice': 'Практическая часть',
    '/polirovka': 'Урок по полировке волос',
    '/memo': 'Памятка по составам'}

LEXICON_LESSONS_NAME: dict[str, str] = {
    '1': 'Урок №1. Определение волоса.',
    '2': 'Урок №2. Третичная структура белка.',
    '3': 'Урок №3. Связи в волосе.',
    '4': 'Урок №4. Строение волоса. Кутикула.',
    '5': 'Урок №5. Строение волос. Кортекс.',
    '6': 'Урок №6. Строение волос. Медула.',
    '7': 'Урок №7. Уровень PH.',
    '8': 'Урок №8. Степени повреждения волос.',
    '9': 'Урок №9. Комплекс Клеточных Мембран.',
    '10': 'Урок №10. Фазы роста волос.',
    '11': 'Урок №11. За счет чего выпрямляются волосы.',
    '12': 'Урок №12. Комплексная реконструкция/холодное восстановление',
    '13': 'Урок №13. Тех.карта кератин.',
    '14': 'Урок №14. Тех.карта ботокс волос.',
    '15': 'Урок №15. Составы, как подобрать нужный.',
    '16': 'Урок №16. Окрашивание + кератин/ботокс.',
    '17': 'Урок №17. Как составить прайс.',
    '18': 'Урок №18. Все о дезинфекции в нашей сфере.',
    '19': 'Урок №19. Исправление неудачной работы.',
    '20': 'Урок №20. Протектор.',
    '21': 'Урок №21. Объясняю почему мои средства могут отличаться от ваших.',
    '22': 'Урок №22. Консультация,поиск, привлечение и удержание клиента.',
    '23': 'Урок №23. Пояснение к презентации домашнего ухода'}

LEXICON_LESSONS_URL: dict[str, str] = {
    '1': 'https://youtu.be/ozxU6x088EY',
    '2': 'https://youtu.be/__qOomkA5gw',
    '3': 'https://youtu.be/SSdK7H1czYo',
    '4': 'https://youtu.be/sUKY3wyqS0o',
    '5': 'https://youtu.be/shU1rWoaKu0',
    '6': 'https://youtu.be/wHSA9W79qFw',
    '7': 'https://youtu.be/mvdfF1bLY2k',
    '8': 'https://youtu.be/wtfFiA2_Gvc',
    '9': 'https://youtu.be/oGCZGCNeUho',
    '10': 'https://youtu.be/sRdCVCzaPmY',
    '11': 'https://youtu.be/yjypCW873Fc',
    '12': 'https://youtu.be/VSJpt-CAY38',
    '13': 'https://youtu.be/pt4Q44pxTyM',
    '14': 'https://youtu.be/4VpbdRonn_I',
    '15': 'https://youtu.be/EDgWH-7IKFE',
    '16': 'https://youtu.be/3kuL5ZKYtas',
    '17': 'https://youtu.be/k918zEWTSeM',
    '18': 'https://youtu.be/NPnT_2GnL4g',
    '19': 'https://youtu.be/hdyZV_1WNDg',
    '20': 'https://youtu.be/4mlRs9JaahI',
    '21': 'https://youtu.be/sQ9YSRBeugs',
    '22': 'https://youtu.be/tLhW9yyMT24',
    '23': 'https://youtu.be/I7qtGD9ygKA',
    'pol': 'https://www.youtube.com/watch?v=cV24v196faA',
    'android': 'https://play.google.com/store/apps/details?id=notion.id&hl=ru&gl=US&pli=1',
    'ios': 'https://apps.apple.com/ru/app/notion-notes-docs-tasks/id1232780281',
    'smm': 'https://www.notion.so/tmnazarkina/OOHHAIR-SMM-4aa428a5a97346e7b3f352358a62aee4',
    'presentation': 'https://disk.yandex.ru/i/6WG_w-V8kDr5oA'}


LEXICON_LESSONS_PRACTICE: dict[str, str] = {
    '1': 'Урок №1. Холодное восстановление/Комплексная реконструкция.',
    '2': 'Урок №2. Kератин.',
    '3': 'Урок №3. Ботокс.'}

LEXICON_LESSONS_PRACTICE_URL: dict[str, str] = {
    '1': 'https://youtu.be/KzxsML5xHaE',
    '2': 'https://youtu.be/qugSdyq2E6A',
    '3': 'https://youtu.be/SypOipkvAr0'}
