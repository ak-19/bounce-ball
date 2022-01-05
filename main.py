import pygame

from Setup import Setup
from Game import Game

setup = Setup()

Game(setup.get_display()).run_game()

setup.quit()