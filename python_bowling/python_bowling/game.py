"""Bowling Game Class"""
from python_bowling.frame import Frame


class Game(object):
    """Game object to take rolls and produce a score"""

    def __init__(self):
        self._score = 0
        self._frame_number = 0
        self._frames = [Frame() for i in range(10)]

    @property
    def score(self):
        """Return the score of a game"""
        return sum(f.score for f in self._frames)

    @property
    def is_open(self):
        """Returns boolean of if the game is completed"""
        return any(f for f in self._frames if f.is_open)

    def _current_frame(self):
        """Returns the current frame object"""
        return self._frames[self._frame_number]

    def frame_numbers_to_score(self):
        """Returns all the frames that need a score added to them"""
        open_frames = [i for i in range(self._frame_number) if self._frames[i].is_open]
        if self._current_frame().is_open:
            open_frames.append(self._frame_number)
        return open_frames

    def roll(self, pins):
        """Roll the ball, knock down pins"""
        for frame in self.frame_numbers_to_score():
            self._frames[frame].roll(pins)

        if self._frame_number < 9 and (self._current_frame().rolls == 2 or pins == 10):
            self._frame_number += 1
