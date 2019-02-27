__all__ = ['get_prizes_table', 'get_consolation_prize', 'init_game']
from model import Game, Question, Answer

def get_prizes_table():
    return prizes_table

def get_consolation_prize():
    return consolation_prize

def init_game():
    return Game(rules, questions)

rules = """
Узнай BattleMC по его цитате. Ответ - ник, под которым он выступает на баттлах. Большие - маленькие буквы, похуй.
/task - напомнить задание
/rules - напомнить правила
"""
wrong_reactions = [
    'Нет',
    'Передохни, подумай',
    'Да ладно тебе, не такие уж и дорогие билеты на Slovo',
    'Камон, серьезно?',
    'Может, ты с ошибкой написал?']
last_wrong_reactions = wrong_reactions + [
    'Почти, последний вопрос!',
    'Не сдавайся! Совсем чуть-чуть осталось']

antihype = 'Е-е-е-е, антихайп, ебал вас всех в рот. Но ответ неправильный.'

questions = [
    Question('Easy, easy, real talk, think about it.',
         [Answer('Oxxxymiron', 'Молодец, аккуратно все написал'),
          Answer('Оксимирон', 'Вообще, Oxxxymiron, но хуй с тобой, засчитано.')],
         [Answer('Мирон', 'Не, ну че ты жида не уважаешь? Напиши правильно!'),
          Answer('Гнойный', antihype),
          Answer('Слава КПСС', antihype),
          Answer('Валентин Дядька', antihype),
          Answer('Птичий пепел', antihype),
          Answer('Бутербродский', antihype),
          Answer('Замай', antihype),
          Answer('Fallen mc', antihype)],
         wrong_reactions),
    Question('Главное - оставаться людьми',
         [Answer('Пиэм', 'На баттле с Паровозом и Майком')],
         [],
         wrong_reactions),
    Question('Этот пиздец моралфагам надолго запомнится.',
         [Answer('Deep-ex-sense', 'Он самый, баттл с Диз-вилсом.'),
          Answer('Wahabeat', 'Так-то ответ правильный, но он бы на тебя обиделся.')],
         [Answer('Rickey f','Его пиздец моралфагам надолго запомнился, да. Цитата принадлежит другому ЭмСи.'),
          Answer('ХХОС', 'Ну, был у него баттл с автором цитаты, но нет.'),
          Answer('Хип-хоп одинокой старухи', 'И не лень же было писать полностью. Но нет, не он.')],
         last_wrong_reactions)]

first_prize = "Первое место!"
second_prize = "Второе место!"
third_prize = "Третье место!"
tenth_prize = "В десятке!"

prizes_table = {1:first_prize,
                2:second_prize,
                3:third_prize}
consolation_prize = "Все призы уже разобрали. Но спасибо, что поучаствовал"
for i in range(4, 11):
    prizes_table[i] = tenth_prize

