from pygame import *


class Snake:

    def __init__(self, player_start):
        self.reset(player_start)
        self.player_start = player_start

    def reset(self, player_start):
        self.x, self.y = player_start

        #0 = Up, 1 = Left, 2 = Down, 3 = Right
        self.facing = 0

        self.length = 1
        self.old_moves = [(self.x,self.y)]
        self.fitness = 0

    def update(self,grid_size,food_coords, turn_values):
        self.turn(turn_values)
        self.move()
        self.eat(food_coords)
        if not self.in_boundries(grid_size): self.reset(self.player_start)

        #Show Snake
        return self.handle_parts()

    def eat(self, food_coords):
        if (self.x,self.y) == tuple(food_coords): self.length += 1
        else: del self.old_moves[0]

    def turn(self, turn_values):
        if turn_values[0]: self.facing = 0
        if turn_values[1]: self.facing = 1
        if turn_values[2]: self.facing = 2
        if turn_values[3]: self.facing = 3

    def in_boundries(self, grid_size):
        if self.x > grid_size[0]: return False
        if self.y > grid_size[0]: return False
        if self.x < 0: return False
        if self.y < 0: return False

        if (self.x,self.y) in self.old_moves[:len(self.old_moves)-2]: return False

        return True

    def move(self):
        if self.facing == 0: self.y -= 1
        elif self.facing == 1: self.x += 1
        elif self.facing == 2: self.y += 1
        elif self.facing == 3: self.x -= 1

        self.old_moves.append((self.x, self.y))


    def handle_parts(self):
        parts = []

        for block in range(self.length):
            coords = self.old_moves[len(self.old_moves)-1-block]
            parts.append(coords)

        return parts