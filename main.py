""" 
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). 
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

    1) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2) Any live cell with two or three live neighbours lives on to the next generation.
    3) Any live cell with more than three live neighbours dies, as if by overpopulation.
    4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

    1) Any live cell with two or three live neighbours survives.
    2) Any dead cell with three live neighbours becomes a live cell.
    3) All other live cells die in the next generation. Similarly, all other dead cells stay dead.


The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; 
births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. 
The rules continue to be applied repeatedly to create further generations.

"""


import pygame
pygame.init()

FPS = 30
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

grid = []
row = []
for i in range(SCREEN_HEIGHT):
    grid.append(row)
    for j in range(SCREEN_WIDTH):
        row.append(0)


scaling_factor = 20
scr = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Life')
cells = []
button = pygame.Rect(10, 10, 50, 30)


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

font = pygame.font.SysFont("Arial", 20)


def renderButton():
    pass
    # button = pygame.Rect(100, 100, 50, 50)


def getNeighbours(cell):

    # Identifying all neighbouring cells
    aboveState = scr.get_at((cell.x,cell.y - 1))
    belowState = scr.get_at((cell.x,cell.y + 1))
    leftState = scr.get_at((cell.x - 1,cell.y))
    rightState = scr.get_at((cell.x + 1,cell.y))
    topLeftState = scr.get_at((cell.x - 1,cell.y - 1))
    topRightState = scr.get_at((cell.x + 1,cell.y - 1))
    bottomLeftState = scr.get_at((cell.x - 1,cell.y + 1))
    bottomRightState = scr.get_at((cell.x + 1,cell.y + 1))

    return aboveState,belowState,leftState,rightState,topLeftState,topRightState,bottomLeftState,bottomRightState



def totalLiving(aboveState,belowState,leftState,rightState,topLeftState,topRightState,bottomLeftState,bottomRightState):
    life_count = 0
    if (aboveState == WHITE):
        life_count += 1
    if (belowState == WHITE):
        life_count += 1
    if (leftState == WHITE):
        life_count += 1
    if (rightState == WHITE):
        life_count += 1
    if (topLeftState == WHITE):
        life_count += 1
    if (topRightState == WHITE):
        life_count += 1
    if (bottomLeftState == WHITE):
        life_count += 1
    if (bottomRightState == WHITE):
        life_count += 1

    return life_count


def updateDead(buffer,x,y):
    # Adjacent cell is not alive, check to see if we can create
    ded_adjacent = pygame.Rect(x, y, 1, 1)
    D_aboveState,D_belowState,D_leftState,D_rightState,D_topLeftState,D_topRightState,D_bottomLeftState,D_bottomRightState = getNeighbours(ded_adjacent)
    living_neighbours = totalLiving( D_aboveState,D_belowState,D_leftState,D_rightState,D_topLeftState,D_topRightState,D_bottomLeftState,D_bottomRightState)
    if (living_neighbours == 3):
        pygame.draw.rect(scr,WHITE,ded_adjacent)
        buffer.append(ded_adjacent)


def beginLife():
    # Checking and killing cells
    buffer = []
    for index,cell in enumerate(cells):

        aboveState,belowState,leftState,rightState,topLeftState,topRightState,bottomLeftState,bottomRightState = getNeighbours(cell)


        # print(cell.x,cell.y)

        # Identifying all neighbouring cells
        # aboveState = scr.get_at((cell.x,cell.y - 1))
        # belowState = scr.get_at((cell.x,cell.y + 1))
        # leftState = scr.get_at((cell.x - 1,cell.y))
        # rightState = scr.get_at((cell.x + 1,cell.y))
        # topLeftState = scr.get_at((cell.x - 1,cell.y - 1))
        # topRightState = scr.get_at((cell.x + 1,cell.y - 1))
        # bottomLeftState = scr.get_at((cell.x - 1,cell.y + 1))
        # bottomRightState = scr.get_at((cell.x + 1,cell.y + 1))

        # print(aboveState)
        life_count = 0

        if (aboveState == WHITE):
            life_count += 1
        else:
            updateDead(buffer, cell.x, cell.y - 1)

        if (belowState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,cell.x,cell.y + 1)

        if (leftState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,cell.x - 1,cell.y)

        if (rightState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,cell.x + 1,cell.y)

        if (topLeftState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,cell.x - 1,cell.y - 1)

        if (topRightState == WHITE):
            life_count += 1
        else: 
            updateDead(buffer,cell.x + 1,cell.y - 1)

        if (bottomLeftState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,cell.x - 1,cell.y + 1)

        if (bottomRightState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,cell.x + 1,cell.y + 1)

        if (life_count < 2 or life_count > 3):
            scr.set_at((cell.x,cell.y), BLACK)
            cells.pop(index)
            grid[cell.y][cell.x] = 0


    for el in buffer:
        cells.append(el)
    print(len(cells))






def drawInitialState():
        # Draw white pixels at mouse location
    if (pygame.mouse.get_pressed()[0] == True):
        x,y = pygame.mouse.get_pos()


        rect = pygame.Rect(x,y,1,1)
        if (len(rect.collidelistall(cells)) == 0):
            # scr.set_at((x,y), WHITE)
            # pygame.draw.rect(scr,WHITE,rect)
            cells.append(rect)
            print(len(cells))




def main():
    clock = pygame.time.Clock()
    running = True
    begin = False
    while running:  

        # Ensure while loop does not go over the capped FPS
        clock.tick(FPS)

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos # gets mouse position
                if button.collidepoint(mouse_pos):
                    # Start the program if the button is pressed
                    begin = True
                    print('button was pressed at {0}'.format(mouse_pos))



        # Draw button
        pygame.draw.rect(scr, [255, 0, 0], button)
        scr.blit(font.render("Begin", False, WHITE), button)




        # Run Conway's Simulation algorithm
        if (begin):
            beginLife()
        else:
            # Draw white pixels at mouse location
            drawInitialState()
            for cell in cells:
                pygame.draw.rect(scr,WHITE,cell)
                grid[cell.y][cell.x] = 1

        # This function will update the contents of the entire display
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()