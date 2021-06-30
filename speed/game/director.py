import random
from time import sleep

from game import constants
from game.score import Score
from game.buffer import Buffer
from game.wordManager import WordManager

from game.actor import Actor
from game.point import Point


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        wordManager (WordManager): controller for all word object
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        buffer (Buffer): input answer(string) from user
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._wordManager = WordManager()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()

        self.actor = Actor()
        self.actor.set_position(Point(0,3))
        self.actor.set_text("abcde")
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        letter = self._input_service.get_letter()
        self._buffer.add_letter(letter)
        self.actor.set_text(letter)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        if random.randint(0,1000) > 960:
            self._wordManager.generate_word()
        self._score.add_points(self._wordManager.check_buffer(self._buffer))
        self._wordManager.move_words()
        self._handle_word_collision()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self._wordManager.get_words())
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self._buffer)

        self._output_service.draw_actor(self.actor)
        self._output_service.flush_buffer()

    def _handle_word_collision(self):
        for word in self._wordManager.get_words():
            if word.get_position().get_y() == constants.MAX_Y - 1:
                self._score.add_points(word.get_points() * -1)
                self._wordManager.get_words().remove(word)