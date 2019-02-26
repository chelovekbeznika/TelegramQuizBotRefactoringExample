# Зачем
Репозиторий существует как попытка показать, как надо рефакторить код, помочь привичь чувство прекрасного в коде.
# Что это
Телеграмм-бот, написанный на python. Совсем простецкий.
Когда бот запускается, начинается игра, где все ведущие диалог с ботом соревнуются друг с другом в ответе на вопросы.
Каждому игроку на старте сообщают правила и первый вопрос.
Вопросы задаются по очереди.
Ответы можно давать маленькими и большими буквами, бот не чувствителен к регистру.
На каждый вопрос может быть несколько правильных ответов. На каждый ответ бот реагирует по разному.
Некоторые ответы "близкие". Бот реагирует на них нестандартно, но не засчитывает, как правильные.
Когда кончаются вопросы, бот фиксирует, на каком месте "финишировал" игрок, и выдаёт ему соответствующий приз в виде строки текста (это может быть, например, ключ в Steam).
На каждый вопрос можно задать набор "совсем неправильных ответов". Если ответ неверен, бот будет выбирать одну из реакций на неправильные ответы случайно.
При попытке игрока отвечать на вопросы после того, как ему был выдан приз, бот реагирует одной и той же репликой вида "успокойся, ты победил"
Бот совсем простецкий, а это значит, что:
Состояние викторины хранится только в памяти, каждый перезапуск бота = игра начинается заново.
Вопросы и ответы тупо вхардкожены (вписаны) в одном из модулей. Я не буду это исправлять, но сделаю так, чтобы этот факт причинял как можно меньше вреда при сопровождении кода.
# Что с этим репозиторием делать
1) Отматывать на Init commit
2) Изучить код в его первозданном и не везде красивом виде (я старался, но писался он наскоро)
3) Открыть лог коммитов
4) наблюдать коммитом за коммитом, как код превращается в конфетку.

Ну, я надеюсь, что воспроизведу именно такой эффект. Отдельное внимание на комментарии к коммитам.
Весь код англоязычен, и первые строки коммитов тоже англоязычны, чтобы было хоть чуть-чуть культурно. Детальные комментарии, чтобы не перетруждать себя и повысить образовательную ценность, буду даны на русском.
# Что внутри (по состоянию на первый коммит)
Три модуля:
- play_bot.py: Тут происходит взаимодействие с API телеграма. Точнее, с уже готовой обёрткой
- model.py: Тут представлены классы, в которых живёт игровая логика
- game_data.py: А тут создаются экземпляры этих классов для использования модулем play_bot.py
- requirements.txt: Это не модуль, это файл, описывающий внешние зависимости

# Как запустить у себя
Тут будет дана самая простая последовательность действий.
1) Поставить python вместе с pip (обязательно), если ещё не
2) Зарегистрироваться в телеграмме, если ещё не
3) Создать бота и получить для него AuthorizationToken. [Процесс описан тут](https://core.telegram.org/bots#3-how-do-i-create-a-bot). Токен запомнить и никому не отдавать! Это ваш "пароль"
4) Скачать/склонировать себе репозиторий
5) Зайти с командной строки в папку с репозиторием и выполнить там "pip install -r requirements.txt"
6) Теперь можно запускать бота. Убедитесь, что у вас есть подключение к интернету, и запустите файл play_bot.py. Желательно, тоже из командной строки.