import pytest
from python_bowling.frame import Frame


@pytest.fixture
def frame():
    return Frame()


def test_frame_roll_count(frame):
    assert frame.rolls == 0
    frame.roll(0)
    assert frame.rolls == 1
    frame.roll(0)
    assert frame.rolls == 2


def test_frame_is_open_with_less_than_two_rolls(frame):
    assert frame.is_open
    frame.roll(0)
    assert frame.is_open
    frame.roll(0)
    assert not frame.is_open
