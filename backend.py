from pygame_functions import *
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

def hasVisited(visited, element):
    for el in visited:
        if (el == element):
            return True
    return False 


def BFS(maze, screen):
    #initialize visited and predecessor
    visited = []
    pred = []
    queue = []
    visited.append(maze.startLocation)
    queue.append(maze.startLocation)
    while queue:
        grid = queue.pop(0)
        for nextGrid in maze.getAdjacencyFrom(grid):
            if (not hasVisited(visited, nextGrid)):
                visited.append(nextGrid)
                nextGrid.predecessor = grid
                if (nextGrid == maze.finishLocation):
                    queue = []
                else:
                    nextGrid.color = BLUE
                    maze.draw(screen)
                    updateDisplay()
                    pause(10)
                    queue.append(nextGrid)

    trace = maze.finishLocation.predecessor
    while (trace != maze.startLocation):
        trace.color = YELLOW
        maze.draw(screen)
        updateDisplay()
        pause(10)
        trace = trace.predecessor






    