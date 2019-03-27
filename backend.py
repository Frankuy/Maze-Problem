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
                    pause(100)
                    queue.append(nextGrid)

    jarak = 0
    trace = maze.finishLocation.predecessor
    while (trace != maze.startLocation):
        trace.color = YELLOW
        jarak += 1
        maze.draw(screen)
        updateDisplay()
        pause(10)
        trace = trace.predecessor

    return jarak

def AStar(maze, screen):
    #initialize visited and predecessor
    visited = []
    pred = []
    queue = []
    visited.append(maze.startLocation)
    queue.append(maze.startLocation)
    jarak = 0
    while queue:
        grid = queue.pop(0)
        jarak = grid.g + 1
        for nextGrid in maze.getAdjacencyFrom(grid):
            if (not hasVisited(visited, nextGrid)):
                nextGrid.g = jarak
                nextGrid.cost = hitungCost(nextGrid.g,nextGrid.i,nextGrid.j,maze.finishLocation.i,maze.finishLocation.j)
                visited.append(nextGrid)
                nextGrid.predecessor = grid
                if (nextGrid == maze.finishLocation):
                    queue = []
                else:
                    nextGrid.color = BLUE
                    maze.draw(screen)
                    updateDisplay()
                    pause(100)
                    insertPriorityCost(queue, nextGrid)

    jarak = 0
    trace = maze.finishLocation.predecessor
    while (trace != maze.startLocation):
        jarak += 1
        trace.color = YELLOW
        maze.draw(screen)
        updateDisplay()
        pause(10)
        trace = trace.predecessor
        
    return jarak

def hitungCost(gn,x1,y1,x2,y2) :
    return gn + abs(x1-x2) + abs(y1-y2)

def insertPriorityCost(queue, grid) :
    if(len(queue)==0)   :
        queue.append(grid)
    else :
        i=0
        found = False
        while(i<len(queue) and not(found)) :
            if(grid.cost < queue[i].cost) :
                found =True
                queue.insert(i,grid)
            else :
                i +=1
        if(not(found)) :
            queue.append(grid)

    






    