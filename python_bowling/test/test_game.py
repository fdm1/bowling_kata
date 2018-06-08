import pytest
from python_bowling.game import Game


@pytest.fixture
def game():
    return Game()


def roll_x_for_rest_of_game(game, pins):
    while game.is_open:
        game.roll(pins)
    return game


def roll_spare(game):
    game.roll(5)
    game.roll(5)


def roll_strike(game):
    game.roll(10)


def test_all_ones(game):
    game = roll_x_for_rest_of_game(game, 1)
    assert game.score == 20


def test_a_spare(game):
    roll_spare(game)
    game.roll(3)
    roll_x_for_rest_of_game(game, 0)
    assert game.score == 16


def test_a_strike(game):
    roll_strike(game)
    game.roll(3)
    game.roll(4)
    roll_x_for_rest_of_game(game, 0)
    assert game.score == 24


def test_mixed_game(game):
    roll_strike(game)
    roll_strike(game)
    roll_spare(game)
    game.roll(5)
    game.roll(0)
    roll_x_for_rest_of_game(game, 0)
    assert game.score == 65


def test_perfect_game(game):
    roll_x_for_rest_of_game(game, 10)
    assert game.score == 300
