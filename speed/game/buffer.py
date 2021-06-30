from game import constants
from game.actor import Actor
from game.point import Point

class Buffer(Actor):
    def __init__(self):
        super().__init__()
        self.set_text("-Buffer: ")
        self.set_position(Point(0, constants.MAX_Y))
    
    def clear(self):
        self.set_text("-Buffer: ")

    def add_letter(self, letter):
        self.set_text(self.get_text() + letter)

    def get_word(self):
        return self.get_text()[constants.WORD:-1]
    
    def get_last_input(self):
        return self.get_text()[-1]