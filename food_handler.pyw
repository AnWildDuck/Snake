from pygame import *
import random

class Food_Handler:

    def __init__(self, player_coords, grid_size):
        self.reset(player_coords, grid_size)


    def reset(self, player_coords, grid_size):
        self.spawn(player_coords, grid_size)


    def spawn(self, player_coords, grid_size):

        x,y = player_coords[0]

        while (x,y) in player_coords:
            x = random.randint(0, grid_size[0]-1)
            y = random.randint(0, grid_size[1]-1)

        self.food = (x,y)


    def check_food(self, player_coords, grid_size):

        if self.food == player_coords[len(player_coords)-1]: self.spawn(player_coords, grid_size);


    def update(self, player_coords, grid_size):
        self.check_food(player_coords, grid_size)

        return self.food