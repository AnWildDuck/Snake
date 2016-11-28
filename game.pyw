from pygame import *
import snake, food_handler

game_scale = (50,50)
grid_size = 10, 10

init()
window = display.set_mode((grid_size[0] * game_scale[0], grid_size[1] * game_scale[1]), RESIZABLE)
clock = time.Clock()


player_start = (grid_size[0]//2,grid_size[1]//2)

player = snake.Snake(player_start)
food = food_handler.Food_Handler(player.old_moves, grid_size)

tick = 1


turn_values = {
        0: False,
        1: False,
        2: False,
        3: False
}
last = 0


while True:

    for e in event.get():
        if e.type == QUIT: quit()
        if e.type == VIDEORESIZE: game_scale = e.w / grid_size[0], e.h / grid_size[1]; window = display.set_mode((int(grid_size[0] * game_scale[0]), int(grid_size[1] * game_scale[1])), RESIZABLE)


    k = key.get_pressed()



    #Get input
    if k[K_UP] and (player.facing != 2 or player.length == 1): turn_values = {0: True, 1: False, 2: False, 3: False,}; last = 0
    if k[K_RIGHT] and (player.facing != 3 or player.length == 1): turn_values = {0: False, 1: True, 2: False, 3: False,}; last = 1
    if k[K_DOWN] and (player.facing != 0 or player.length == 1): turn_values = {0: False, 1: False, 2: True, 3: False,}; last = 2
    if k[K_LEFT] and (player.facing != 1 or player.length == 1): turn_values = {0: False, 1: False, 2: False, 3: True,}; last = 3




    #Game thing

    go = 0.5
    tick += clock.tick()/1000
    if tick > go:

        food_coords = food.update(player.old_moves, grid_size)
        player_coords = player.update(grid_size, food_coords, turn_values)

        window.fill((40, 40, 40))


        draw.rect(window, (200, 150, 0), (food_coords[0] * game_scale[0], food_coords[1] * game_scale[1], game_scale[0], game_scale[1]))

        for x, y in player_coords:
            index = player_coords.index((x, y))
            c = 255*(index/len(player_coords))
            draw.rect(window, (c, 200, c), (x * game_scale[0], y * game_scale[1], game_scale[0], game_scale[1]))

        win = window.copy()

        tick -= go

    try: window.blit(win,(0,0))
    except: pass

    f = font.SysFont('', int(min(game_scale[0], game_scale[1]) / 2))
    message1 = f.render(str(player.length-1), 0, (200, 200, 200))
    window.blit(message1, (game_scale[0] / 20, game_scale[1] / 20))

    display.update()
