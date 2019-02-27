from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from game_data import init_game, get_prizes_table, get_consolation_prize
import logging
import urllib

def main():
    updater = create_bot()
    tune_bot(updater)
    start_bot(updater)

def create_bot():
    with open('BotToken.txt', 'r') as key_file:
        telegram_bot_api_key = key_file.read()
    return Updater(telegram_bot_api_key)

def tune_bot(updater):
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', handle_start_command))
    dp.add_handler(CommandHandler('rules', handle_rules_command))
    dp.add_handler(CommandHandler('task', handle_task_command))
    dp.add_handler(MessageHandler(Filters.text, process_answer))
    dp.add_error_handler(handle_error)

def start_bot(updater):
    updater.start_polling()
    updater.idle()

def handle_start_command(bot, update):
    if not get_user_id(update) in games:
        games[get_user_id(update)] = init_game()
    handle_rules_command(bot, update)
    handle_task_command(bot, update)

def user_update_handler(handler):
    """
    Декоратор с общим поведением. Гарантирует перед выполнением handler следующее:
    1) Игра уже запущена
    2) Игра еще не закончена
    Все, что не соответствует данному инварианту обрабатывается прямо тут функцией
    """
    def common_handler(bot, update):
        user_id = get_user_id(update)
        if user_id in games:
            if not games[user_id].completed():
                handler(bot, update)
            else:
                reply(update.message, 'Успокойся, ты уже выиграл! Вот приз:')
                reply(update.message, form_prize(user_id))
        else:
            handle_start_command(bot, update)
            
    return common_handler

@user_update_handler
def handle_rules_command(bot, update):
    game = games[get_user_id(update)]
    reply(update.message, game.tell_rules())

@user_update_handler
def handle_task_command(bot, update):
    game = games[get_user_id(update)]
    question_intro = 'Задание #{0}:'.format(game.question_number + 1)
    reply(update.message, question_intro)
    reply(update.message, game.tell_question())

@user_update_handler
def process_answer(bot, update):
    user_id = get_user_id(update)
    game = games[user_id]
    value = update.message.text.strip()
    reaction = game.check_answer(value)
    reply(update.message, reaction)
    if game.completed():
        position = determine_position(user_id)
        prize = form_prize(position)
        reply(update.message, prize)
    if not game.completed() and not game.question_told:
        handle_task_command(bot, update)

def reply(message, text):
    message.reply_text(text)

def get_user_id(update):
    return update.message.from_user.id

def determine_position(user_id):
    if not user_id in winners:
        winners[user_id] = len(winners) + 1
    return winners[user_id]    

def form_prize(position):
    prizes_table = get_prizes_table()
    if position in prizes_table:
        return prizes_table[position]
    else:
        consolation_prize = get_consolation_prize()
        return consolation_prize

def handle_error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def create_logger():
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=log_format, level=logging.INFO)
    return logging.getLogger(__name__)

if __name__ == '__main__':
    logger = create_logger()
    games = dict()
    winners = dict()
    main()
