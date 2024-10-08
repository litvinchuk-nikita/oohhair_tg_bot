LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': f'Привет!\nЗапрос на открытие доступа к курсу отправлен💌\n'
              'Дай мне несколько минут для одобрения и я открою тебе первые уроки🧠',
    'open_th': f'Доступ к теоритической части курса открыт🤍\nДля ознакомления с функционалом бота введите /help',
    'open_pr': f'Доступ к практической части курса\nоткрыт🤍\nДля ознакомления с функционалом бота введите /help',
    'open_prom': f'Доступ к курсу по повышению квалификации открыт🤍\nДля ознакомления с функционалом бота введите /help',
    'open_polir': f'Доступ к уроку по полировке волос открыт🤍\nДля ознакомления с функционалом бота введите /help',
    'open_smm': f'Доступ к разделу по СММ открыт🤍\nДля ознакомления с функционалом бота введите /help',
    'open': f'Доступ к курсу открыт🤍\nДля ознакомления с функционалом бота введите /help',
    'close': 'Доступ закрыт',
    '/help': f'Привет, этот бот предназначен для прохождения курса в OOHHAIR SCHOOL\n\n'
             f'Доступные команды:\n/start - Отправить запрос доступа к курсу\n'
             f'/theory - Теоритическая часть\n'
             f'/smm -  Основы СММ\n/practice - Практическая часть\n'
             f'/polirovka - Урок по полировке волос\n'
             f'/promotion - Курс по повышению квалификации\n'
             f'/memo - Памятка по составам\n'
             f'/reminder - Памятка по технике работы\n'
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
    '/promotion': 'Первые два урока обязательно посмотреть до встречи и сделать памятку в тетради или заметках😊',
    '/memo': f'<b>Выбери состав по силе выпрямления, который тебе нужен:</b>\n\n* Сила состава в легкие-средние и средние-сильные зависит от техники вашей работы',
    'strong': f'Макадамия Viure, Максвел Революшн, Кофе Премиум, Кофе Стрейч, Кофе Смэш, Max Blowout',
    'middlestrong': f'Нутримакс Экстрим, Дефинитив Viure, Космо павер',
    'middle': f'Органопластия премиум, ББ Пластия, Гидра, Кофе Верде, Биксипластия Маракуя, Лимба павер',
    'light': f'Все ботоксы, мэджик браш, органопластия блонд, Сhoose',
    'lightmiddle': f'Ultra Recovery, Лимба лайт, Микс протеин, Коллаген happy hair',
    'other': f'Не понимаю вас..\nДля ознакомления с возможностями бота введите команду /help',
    'final': f'Ура! Поздравляю, теперь ты знаешь все, осталось все освоить на практике.\n'
             'Не стесняйся возвращаться и пересматривать видео несколько раз🫶🏻',
    'injury': f'<b>Выбери степень повреждения и толщину волоса:</b>\n\n* Одинаковый результат на средние волосы со средним завитком:\n'
              f'1. Температура: 190, толщина пряди 0,5см, протяжки: корень - 15, длина - 10,\nконцы - 7\n'
              f'2. Температура: 220-230, толщина пряди 1-1,5см, протяжки: корень - 10-13, длина - 6-8, концы - 3-4',
    '1/2 thin': f'Ровный/легкий завиток - легкий кератин/ботоксы.\nТемпература: 180-210\n\n'
                f'Средний завиток - легкий/легкий-средний кератин.\nТемпература: 190-210\n\n'
                f'Сильный завиток - средний кератин.\nТемпература: 200-220',
    '1/2 middle': f'Ровный/легкий завиток - легкий/легкий-средний кератин.\nТемпература: 200-210\n\n'
                  f'Средний завиток - средний кератин.\nТемпература: 210-230\n\n'
                  f'Сильный завиток - средний-сильный/сильный кератин.\nТемпература: 220-230',
    '1/2 fat': f'Ровный/легкий завиток - средний кератин.\nТемпература: 210-220\n\n'
               f'Средний завиток - средний-сильный/сильный кератин.\nТемпература: 220-230\n\n'
               f'Сильный завиток - сильный кератин.\nТемпература: 220-230',
    '3/4 thin': f'Ровный/легкий завиток - легкий кератин/ботоксы.\nТемпература: 160-190\n\n'
                f'Средний завиток - легкий кератин.\nТемпература: 160-200\n\n'
                f'Сильный завиток - легкий-средний кератин.\nТемпература: 180-210',
    '3/4 middle': f'Ровный/легкий завиток - легкий/легкий-средний кератин.\nТемпература: 160-210\n\n'
                  f'Средний завиток - легкий-средний кератин.\nТемпература: 160-210\n\n'
                  f'Сильный завиток - средний кератин.\nТемпература: 160-220',
    '3/4 fat': f'Ровный/легкий завиток - легкий-средний/средний кератин.\nТемпература: 180-210\n\n'
               f'Средний завиток - средний кератин.\nТемпература: 180-220\n\n'
               f'Сильный завиток - средний/средний-сильный кератин.\nТемпература: 180-220'}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'Отправить запрос доступа к курсу',
    '/help': 'Справка по работе бота',
    '/theory': 'Теоритическая часть',
    '/smm': 'Основы СММ',
    '/practice': 'Практическая часть',
    '/polirovka': 'Урок по полировке волос',
    '/promotion': 'Курс по повышению квалификации',
    '/memo': 'Памятка по составам',
    '/reminder': 'Памятка по технике работы'}

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
    '12': 'Урок №12. Процедура - Холодное восстановление',
    '13': 'Урок №13. Холодное восстановление перед кератином/ботоксом (комплексная реконструкция)',
    '14': 'Урок №14. Тех.карта кератин.',
    '15': 'Урок №15. Тех.карта ботокс волос.',
    '16': 'Урок №16. Составы, как подобрать нужный.',
    '17': 'Урок №17. Окрашивание + кератин/ботокс.',
    '18': 'Урок №18. Как составить прайс.',
    '19': 'Урок №19. Все о дезинфекции в нашей сфере.',
    '20': 'Урок №20. Исправление неудачной работы.',
    '21': 'Урок №21. Протектор.',
    '22': 'Урок №22. Объясняю почему мои средства могут отличаться от ваших.',
    '23': 'Урок №23. Консультация,поиск, привлечение и удержание клиента.',
    '24': 'Урок №24. Пояснение к презентации домашнего ухода'}

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
    '12': 'https://youtu.be/_73cMH6TF7o?si=VLA4prboCAQRuedt',
    '13': 'https://youtu.be/p8kCbOMEgR0?si=bBDEm8LWDZgYswhr',
    '14': 'https://youtu.be/pt4Q44pxTyM',
    '15': 'https://youtu.be/4VpbdRonn_I',
    '16': 'https://youtu.be/EDgWH-7IKFE',
    '17': 'https://youtu.be/3kuL5ZKYtas',
    '18': 'https://youtu.be/k918zEWTSeM',
    '19': 'https://youtu.be/NPnT_2GnL4g',
    '20': 'https://youtu.be/hdyZV_1WNDg',
    '21': 'https://youtu.be/4mlRs9JaahI',
    '22': 'https://youtu.be/sQ9YSRBeugs',
    '23': 'https://youtu.be/tLhW9yyMT24',
    '24': 'https://youtu.be/I7qtGD9ygKA',
    'pol': 'https://www.youtube.com/watch?v=cV24v196faA',
    'android': 'https://play.google.com/store/apps/details?id=notion.id&hl=ru&gl=US&pli=1',
    'ios': 'https://apps.apple.com/ru/app/notion-notes-docs-tasks/id1232780281',
    'smm': 'https://www.notion.so/tmnazarkina/OOHHAIR-SMM-4aa428a5a97346e7b3f352358a62aee4',
    'presentation': 'https://disk.yandex.ru/i/6WG_w-V8kDr5oA'}


LEXICON_LESSONS_PRACTICE: dict[str, str] = {
    '1': 'Урок №1. Kератин.',
    '2': 'Урок №2. Ботокс.'}

LEXICON_LESSONS_PRACTICE_URL: dict[str, str] = {
    '1': 'https://youtu.be/qugSdyq2E6A',
    '2': 'https://youtu.be/SypOipkvAr0'}

LEXICON_LESSONS_PROMOTION: dict[str, str] = {
    '1': 'Урок №1. Нанопластика',
    '2': 'Урок №2. Нанопластика на повтор',
    '3': 'Урок №3. Уровень PH',
    '4': 'Урок №4. Умный прайс',
    '5': 'Урок №5. Как исправить работу',
    '6': 'Урок №6. Привлечение клиентов',
    '7': 'Урок №7. Пояснение к презентации домашнего ухода'}

LEXICON_LESSONS_PROMOTION_URL: dict[str, str] = {
    '1': 'https://youtu.be/6tQ1eUtuYiY?si=ckige7hTdaM92Bq9',
    '2': 'https://youtu.be/trq06SDgMws?si=2d_WeRPByWCuyoNX',
    '3': 'https://youtu.be/mvdfF1bLY2k?si=A6DZdAmrgURVsZyA',
    '4': 'https://youtu.be/k918zEWTSeM?si=tLP476J3VgE8k7im',
    '5': 'https://youtu.be/hdyZV_1WNDg?si=AhN0AxHpMl7Qo15w',
    '6': 'https://youtu.be/tLhW9yyMT24?si=GPtYzStA0Z3lsWkw',
    '7': 'https://youtu.be/I7qtGD9ygKA?si=FTj64882jOTYqbHH'}