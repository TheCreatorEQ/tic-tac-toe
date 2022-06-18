import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN


pygame.init()

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
grid = [[0 for i in range(3)] for i in range(3)]
record = None
turn = 1


screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def draw_xo():
    if record[1] <= 200:
        if record[0] <= 200:
            grid[0][0] = turn

        if record[0] >= 200 and record[0] <= 400:
            grid[0][1] = turn
 
        if record[0] >= 400 and record[0] <= 600:
            grid[0][2] = turn


    if record[1] >= 200 and record[1] <= 400:
        if record[0] <= 200:
            grid[1][0] = turn

        if record[0] >= 200 and record[0] <= 400:
            grid[1][1] = turn


        if record[0] >= 400 and record[0] <= 600:
            grid[1][2] = turn


    if record[1] >= 400 and record[1] <= 600:
        if record[0] <= 200:
            grid[2][0] = turn
        if record[0] >= 200 and record[0] <= 400:
            grid[2][1] = turn
        if record[0] >= 400 and record[0] <= 600:
            grid[2][2] = turn

    

def draw():
    for y in range(3):
        for x in range(3):
            if grid[y][x] == 1:
                pygame.draw.circle(screen, (0,0,0), ((x+1)*100 + x*100,(y+1)*100 + y*100), 30)
            if grid[y][x] == 2:
                pygame.draw.circle(screen, (255,0,0), ((x+1)*100 + x*100,(y+1)*100 + y*100), 30)
                
     



running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            record = event.pos
            draw_xo()
            if turn == 1:
                turn = 2
            elif turn == 2:
                turn = 1
    # EVENT HANDLING




    # GAME STATE UPDATES
    # All game math and comparisons happen here


    # DRAWING
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(200, 0, 10, 600))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(400, 0, 10, 600))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 200, 600, 10))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 400, 600, 10))
    draw()
    


    



    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
