from pygame_functions import *
from backend import *
from copy import *
import sys

sys.setrecursionlimit(10000)
args = sys.argv
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Grid:
    def __init__(self, gridType, xpos, ypos, i, j, gridSize):
        self.gridType = gridType #1 for obstacle, 0 for no obstacle
        if (self.gridType == '0'):
            self.color = WHITE
        elif (self.gridType == '1'):
            self.color = BLACK
        self.location = (xpos,ypos)
        self.gridSize = gridSize
        self.cost = 0
        self.g = 0
        self.predecessor = None
        self.adjacency = None
        self.i = i
        self.j = j

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, [self.location[0], self.location[1], self.gridSize, self.gridSize])

    def changeColor(self, color):
        self.color = color

    def changeCost(self, cost):
        self.cost = cost

class Maze:
    def __init__(self, width, height, inputMatrix):
        self.width = width
        self.height = height
        self.matrix = []
        self.startLocation = None
        self.finishLocation = None

        gridSize = int(width/len(inputMatrix))
        i = 0
        for row in inputMatrix:
            j = 0
            line = []
            for element in row:
                newGrid = Grid(element, gridSize*j + 30, gridSize*i + 70, i, j, gridSize)
                line.append(newGrid)
                j += 1
            self.matrix.append(line)
            i += 1

        for row in self.matrix:
            for element in row:
                if (element.gridType == '0'):
                    self.searchAdjacency(element)

    def draw(self, screen):
        for row in self.matrix:
            for element in row:
                element.draw(screen)

    def setStartLocation(self, mouseX, mouseY):
        for row in maze.matrix:
            for element in row:
                if (element.gridType == '0'):
                    if (self.mouseChecker(element, mouseX, mouseY)):
                        element.color = RED
                        self.startLocation = element
                        return True

    def setFinishLocation(self, mouseX, mouseY):
        for row in maze.matrix:
            for element in row:
                if (element.gridType == '0'):
                    if (self.mouseChecker(element, mouseX, mouseY)):
                        element.color = GREEN
                        self.finishLocation = element
                        return True

    def mouseChecker(self, element, mouseX, mouseY):
        return mouseX >= element.location[0] and mouseX <= element.location[0] + element.gridSize and mouseY >= element.location[1] and mouseY <= element.location[1] + element.gridSize
    
    def searchAdjacency(self, grid):
        i = 0
        adjacency = []
        for row in self.matrix:
            j = 0
            for element in row:
                if (grid == element):
                    #RIGHT FROM GRID
                    if (i + 1 < len(self.matrix)):
                        if (self.matrix[i + 1][j].gridType == '0'):
                            adjacency.append(self.matrix[i + 1][j])
                    #UP FROM GRID
                    if (j - 1 >= 0):
                        if (self.matrix[i][j - 1].gridType == '0'):
                            adjacency.append(self.matrix[i][j - 1])
                    #LEFT FROM GRID
                    if (i - 1 >= 0):
                        if (self.matrix[i - 1][j].gridType == '0'):
                            adjacency.append(self.matrix[i - 1][j])
                    #DOWN FROM GRID
                    if (j + 1 < len(self.matrix)):
                        if (self.matrix[i][j + 1].gridType == '0'):
                            adjacency.append(self.matrix[i][j + 1])
                j+=1
            i+=1
        grid.adjacency = adjacency

    def getAdjacencyFrom(self, grid):
        for row in self.matrix:
            for element in row:
                if (grid == element):
                    return element.adjacency

# Make matrix of maze
if (len(args) == 2):
    mazefile = open(args[1], "r")
else:
    print('Enter maze file :')
    mazefile = input()
    mazefile = open(mazefile, "r")

inputMatrix = []
for line in mazefile:
    row = []
    for char in line:
        if (char != '\n'):
            row.append(char)
    inputMatrix.append(row)
mazefile.close()

screen = screenSize(800,600)
pygame.display.set_caption("Grid Test")
setBackgroundColour('white')

maze = Maze(500,500,inputMatrix)
bfsButton = makeSprite("image/button_bfs.png")
moveSprite(bfsButton, 600,300)
showSprite(bfsButton)
aStarButton = makeSprite("image/button_a.png")
moveSprite(aStarButton, 600,400)
showSprite(aStarButton)
mapSize = makeLabel(str(len(inputMatrix))+ " x "+ str(len(inputMatrix)), 50,600,200)
showLabel(mapSize)
selectStart = makeLabel("Select START location",50,30,0)
selectFinish = makeLabel("Select FINISH location",50,30,0)
selectAlgo = makeLabel("Select ALGORITHM",50,30,0)
showLabel(selectStart)
logo = makeSprite("image/logo2.png")
moveSprite(logo, 550, 50)
showSprite(logo)
startMaze = None
jarakLabel = None

run = True
start = True
finish = False
while run:
    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #DRAWING MAZE
    maze.draw(screen)

    #ASKING START AND FINISH LOCATION
    if (mousePressed()):
        if (start):
            if (finish):
                if (maze.setFinishLocation(mouseX(), mouseY())):
                    start = False
                    hideLabel(selectFinish)
                    showLabel(selectAlgo)
                    startMaze = copy(maze)
            else:
                if (maze.setStartLocation(mouseX(), mouseY())):
                    finish = True
                    hideLabel(selectStart)
                    showLabel(selectFinish)
                    pause(200)

    #ASKING ALGORITHM
    if (maze.startLocation != None and maze.finishLocation != None):
        if (spriteClicked(bfsButton)):
            hideLabel(jarakLabel)
            maze = deepcopy(startMaze)
            pause(100)
            jarak = BFS(maze, screen)
            jarakLabel = makeLabel("Jarak : " + str(jarak), 50, 600, 500)
            showLabel(jarakLabel)
        
        if (spriteClicked(aStarButton)):
            hideLabel(jarakLabel)
            maze = deepcopy(startMaze)
            pause(100)
            jarak = AStar(maze, screen)
            jarakLabel = makeLabel("Jarak : " + str(jarak), 50, 600, 500)
            showLabel(jarakLabel)

    #UPDATE SURFACE
    updateDisplay()
    tick(60)

pygame.quit()