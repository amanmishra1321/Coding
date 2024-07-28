def makeRottenOrange(grid,row,col):
    if (row >= 0 and row<len(grid) and col>=0 and col<len(grid[0]) and grid[row][col] == 2):
        if (row -1 >= 0 and grid[row][col] == 1):
            grid[row-1][col] = 2
        if((row+1) < len(grid)  and grid[row][col] == 1):
            grid[row+1][col] = 2
        if((col-1 >= 0) and grid[row][col] == 1):
            grid[row][col-1] = 2
        if((col+1 < 0) and grid[row][col] == 1):
            grid[row][col+1] = 2
            
def checkIfFreshTomatoAvailable(grid,row,col):
    if row-1>=0 and grid[row-1][col] == 1:
        return True
    if row+1<len(grid) and grid[row+1][col] == 1:
        return True
    if col+1<len(grid[0]) and grid[row][col+1] == 1:
        return True
    if col-1>=0 and grid[row][col-1] == 1:
        return True
    return False

def orangesRotting(grid):
    n = len(grid)
    m = len(grid[0])
    ans = 0
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 2 and checkIfFreshTomatoAvailable(grid,row,col):
                print(grid,row,col)
                makeRottenOrange(grid,row,col)
                ans += 1
                print(grid)

    for row in range(n):
        for col in range(m):
            if checkIfFreshTomatoAvailable(grid,row,col):
                return -1

    return ans
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))