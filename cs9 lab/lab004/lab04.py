from Stack import Stack
def solveMaze(maze, startX, startY):
    if maze == []:
        return False
    num = 1
    path = Stack()
    X = startX
    Y = startY
    path.push([X,Y])
    maze[X][Y] = num
    found = False
    while path.isEmpty() == False and found == False:
        if X != 0:
            if maze[X-1][Y] == 'G':
                found = True
                continue
            elif maze[X-1][Y] == ' ':
                num += 1
                X = X-1
                path.push([X,Y])
                maze[X][Y] = num
                continue
        if Y != len(maze[0])-1:
            if maze[X][Y+1] == 'G':
                found = True
                continue
            elif maze[X][Y+1] == ' ':
                num += 1
                Y = Y+1
                path.push([X,Y])
                maze[X][Y] = num
                continue
        if X != len(maze)-1:
            if maze[X+1][Y] == 'G':
                found = True
                continue
            elif maze[X+1][Y] == ' ':
                num += 1
                X = X+1
                path.push([X,Y])
                maze[X][Y] = num
                continue
        if Y != 0:
            if maze[X][Y-1] == 'G':
                found = True
                continue
            elif maze[X][Y-1] == ' ':
                num += 1
                Y = Y-1
                path.push([X,Y])
                maze[X][Y] = num
                continue
        path.pop()
        if path.isEmpty() == False:
            X = path.peek()[0]
            Y = path.peek()[1]
    if found == True:
        return True
    if path.isEmpty() == True:
        return False

