import pytest
import game_of_life as game_of_life

def test_start():
    game = game_of_life.Board([(0,0),(1,1)])
    assert game

def test_count_no_neighbouts():
    game = game_of_life.Board([(0,0),(1,1)])
    assert game.count_no_neighbours(0,0) == 1

def test_turn_block():
    game = game_of_life.Board([(0,0),(0,1),(1,1),(1,0)])
    game.turn()
    assert len(game.data) == 4

def test_turn_blinker():
    game = game_of_life.Board([(0,0),(0,1),(0,2)])
    game.turn()
    game.turn()
    assert (0,0) in game.data
    assert (0,1) in game.data
    assert (0,2) in game.data
