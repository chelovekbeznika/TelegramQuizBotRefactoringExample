import random

class Game:
    def __init__(self, rules, questions):
        self.question_number = 0
        self.rules = rules
        self.questions = questions
        self.objective_told = False

    def tell_rules(self):
        return self.rules

    def tell_question(self):
        self.question_told = True
        return self.current_question.tell_question()

    def check_answer(self, value):
        result, reaction = self.current_question.check_answer(value)
        if result:
            self.objective_told = False
            self.question_number += 1
        return reaction

    def completed(self):
        return self.question_number >= len(self.questions)

    @property
    def current_question(self):
        return self.questions[self.question_number]

class Question:
    def __init__(self, objective, right_answers, close_answers, wrong_reactions):
        self.objective = objective
        self.right_answers = right_answers
        self.close_answers = close_answers
        self.wrong_reactions = wrong_reactions

    def tell_question(self):
        return self.objective

    def check_answer(self, value):
        for variant in self.right_answers:
            if variant.check_answer(value):
                return True, variant.get_reaction()
        for variant in self.close_answers:
            if variant.check_answer(value):
                return False, variant.get_reaction()
        return False, random.choice(self.wrong_reactions)

class Answer:
    def __init__(self, value, reaction):
        self.value = value.lower()
        self.reaction = reaction

    def check_answer(self, answer):
        return self.value == answer.lower()

    def get_reaction(self):
        return self.reaction
