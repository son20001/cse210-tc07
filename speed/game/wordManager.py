import random
from game import constants
from game.word import Word

class WordManager():
    """A nutritious substance that snake's like. The responsibility of Word is to keep track of its appearance and position. A Word can move around randomly if asked to do so. 
    
    Stereotype:
        Information Holder

    Attributes: 
        words (list): all words in the screen
    """
    def __init__(self):
        self._words = []
    
    def generate_word(self):
        word = Word()
        self._words.append(word)
    
    def get_words(self):
        return self._words
    
    def check_buffer(self, buffer):
        score = 0

        if buffer.get_last_input() == "*":
            buff_word = buffer.get_word()
            for word in self._words:
                if buff_word == word.get_text():
                    score = word.get_points()
                    break
                else:
                    score = word.get_points() * -1
            self._words.remove(word)
            buffer.clear()

        return score

    def move_words(self):
        for word in self._words:
            word.move_next()
