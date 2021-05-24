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
import copy
pygame.init()

FPS = 200
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000



# scaling_factor = 20
scr = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Life')
cells = []


""" Below are the predefine seeds for some well known structures in Conway's Simulation
Uncomment the wanted seed below, and comment out drawInitialState() function in the main while loop to observe """

# Oscillators
# cells.append((100,100))
# cells.append((101,100))
# cells.append((102,100))


# Still lifes
# cells.append((100,100))
# cells.append((101,100))
# cells.append((100,101))
# cells.append((101,101))


# Beacon
# cells.append((100,100))
# cells.append((101,100))
# cells.append((100,101))
# cells.append((101,101))

# cells.append((102,102))
# cells.append((103,102))
# cells.append((102,103))
# cells.append((103,103))


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
        # pygame.draw.rect(scr,WHITE,ded_adjacent)
        buffer.append((x,y))


def beginLife():
    # Checking and killing cells
    buffer = []
    to_remove = []
    new_cells = copy.deepcopy(cells)
    for index,cell in enumerate(new_cells):

        Rcell = pygame.Rect(cell[0],cell[1],1,1)
        aboveState,belowState,leftState,rightState,topLeftState,topRightState,bottomLeftState,bottomRightState = getNeighbours(Rcell)



        # print(aboveState)
        life_count = 0

        if (aboveState == WHITE):
            life_count += 1
        else:
            updateDead(buffer, Rcell.x, Rcell.y - 1)

        if (belowState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,Rcell.x,Rcell.y + 1)

        if (leftState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,Rcell.x - 1,Rcell.y)

        if (rightState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,Rcell.x + 1,Rcell.y)

        if (topLeftState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,Rcell.x - 1,Rcell.y - 1)

        if (topRightState == WHITE):
            life_count += 1
        else: 
            updateDead(buffer,Rcell.x + 1,Rcell.y - 1)

        if (bottomLeftState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,Rcell.x - 1,Rcell.y + 1)

        if (bottomRightState == WHITE):
            life_count += 1
        else:
            updateDead(buffer,Rcell.x + 1,Rcell.y + 1)

        if (life_count < 2 or life_count > 3):
            to_remove.append(cell)


    
    buffer = set(buffer)
    for ded in to_remove:
        scr.set_at((ded[0],ded[1]), BLACK)
        cells.remove(ded)
    for el in buffer:
        cells.append((el[0],el[1]))
        scr.set_at((el[0],el[1]), WHITE)

    print(len(cells))






def drawInitialState():
        # Draw white pixels at mouse location
    if (pygame.mouse.get_pressed()[0] == True):
        x,y = pygame.mouse.get_pos()


        rect = pygame.Rect(x,y,1,1)
        # if (len(rect.collidelistall(cells)) == 0):
            # scr.set_at((x,y), WHITE)
            # pygame.draw.rect(scr,WHITE,rect)
        cells.append((x,y))
        pygame.draw.rect(scr,WHITE,rect)
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

        # This function will update the contents of the entire display
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()