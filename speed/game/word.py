import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """A nutritious substance that snake's like. The responsibility of Word is to keep track of its appearance and position. A Word can move around randomly if asked to do so. 
    
    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the Word is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the Word to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self._points = 0
        self.set_text(constants.LIBRARY[random.randint(0,len(constants.LIBRARY))])
        self.reset()
    
    def get_points(self):
        """Gets the points this Word is worth.
        
        Args:
            self (Word): an instance of Word.

        Returns:
            integer: The points this Word is worth.
        """
        return self._points

    def reset(self):
        """Resets the Word by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
        
        Args:
            self (Word): an instance of Word.
        """
        self._points = len(self._text) * 10
        x = random.randint(1, constants.MAX_X - 2 - len(self._text))
        y = 1
        position = Point(x, y)
        vx = 0
        vy = 1
        velocity = Point(vx, vy)
        self.set_position(position)
        self.set_velocity(velocity)
        
