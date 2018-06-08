"""A place for holding the status of frames"""

class Frame(object):
    """Frame object to track score of frames"""

    def __init__(self):
        self._rolls = 0
        self._score = 0
        self._is_strike = False

    @property
    def is_open(self):
        """Return if the frame is scoreable:

        if not yet had two rolls
        if two rolls made and score is currently 10 (spare)
        """
        return (
            self.rolls < 2
            or (self.score == 10 and self.rolls == 2)  # spare
            or (self._is_strike and self.rolls < 3)  # strike
        )

    @property
    def score(self):
        """Return the score for a frame"""
        return self._score

    @property
    def rolls(self):
        """Return the number of rolls counted for a frame"""
        return self._rolls

    def roll(self, pins):
        """Add the roll and score to the frame"""
        if pins == 10 and self.rolls == 0:
            self._is_strike = True
        self._rolls += 1
        self._score += pins
