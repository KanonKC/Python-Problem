maze = []
visited = []

def dfs(i,j):    
    if i < 0 or j < 0 or i >= len(maze) or j >= len(maze[0]) or maze[i][j] == "#" or visited[i][j] == 1:
        return False
    elif maze[i][j] == "X":
        return True
    
    visited[i][j] = 1
    return dfs(i+1,j) or dfs(i,j+1) or dfs(i-1,j) or dfs(i,j-1)
    
while True:
    tile = input()
    if tile == "":
        break
    maze.append(tile)
    visited.append([0 for i in range(len(tile))])

si,sj = 0,0
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            si,sj = i,j
            break

if dfs(si,sj):
    print("Possible to walk from S to X")
else:
    print("Impossible to walk from S to X")
    
"""
#######
#S...X#
#######
"""

"""
#######
#S.#.X#
#######
"""

"""
################
#..............#
#.####.#######.#
#.####.#######.#
#.####.#######.#
#.############.#
#S.##.X........#
################
"""

"""
################
#.......#......#
#.......#......#
#...S...#..X...#
#.......#......#
#.......#......#
#.......#......#
################
"""