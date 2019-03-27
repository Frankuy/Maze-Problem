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
    jarak=0
    visited.append(maze.startLocation)
    queue.append(maze.startLocation)
    while queue:
        jarak += 1
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
                    pause(200)
                    queue.append(nextGrid)

    trace = maze.finishLocation.predecessor
    while (trace != maze.startLocation):
        trace.color = YELLOW
        maze.draw(screen)
        updateDisplay()
        pause(10)
        trace = trace.predecessor

def AStar(maze, screen):
    #initialize visited and predecessor
    visited = []
    pred = []
    queue = []
    jarak = 0
    visited.append(maze.startLocation)
    queue.append(maze.startLocation)
    while queue:
        jarak += 1
        grid = queue.pop(0)
        for nextGrid in maze.getAdjacencyFrom(grid):
            if (not hasVisited(visited, nextGrid)):
                nextGrid.cost = hitungCost(jarak,nextGrid.location[0],nextGrid.location[1],maze.finishLocation.location[0],maze.finishLocation.location[1])

                visited.append(nextGrid)
                nextGrid.predecessor = grid
                if (nextGrid == maze.finishLocation):
                    queue = []
                else:
                    nextGrid.color = BLUE
                    maze.draw(screen)
                    updateDisplay()
                    pause(200)
                    insertPriorityCost(queue, nextGrid)

    trace = maze.finishLocation.predecessor
    while (trace != maze.startLocation):
        trace.color = YELLOW
        maze.draw(screen)
        updateDisplay()
        pause(10)
        trace = trace.predecessor

def hitungCost(gn,x1,y1,x2,y2) :
    return gn + abs((x1-x2)*(x1-x2)) + abs((y1-y2)*(y1-y2))

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
    for j in queue :
        print(j.cost)
    print()
