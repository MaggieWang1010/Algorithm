
class Solution:

    def hasPath(self, maze: list[list[int]], start: list[int],
                destination: list[int]) -> bool:
        # left, right, up, down
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # width
        n = len(maze)
        # height
        m = len(maze[0])

        def dfs(visited: list[list[int]], st: list[int]):
            # if return to a visited point, end
            if visited[st[0]][st[1]]:
                return False
            # Reach the destination, end
            if st[0] == destination[0] and st[1] == destination[1]:
                return True
            # record the current point as visited
            visited[st[0]][st[1]] = True
            # go through all directions
            for d in dir:
                # try to move one step
                x = st[0] + d[0]
                y = st[1] + d[1]
                # while in the maze and the last move is valid
                while x >= 0 and x < n and y >= 0 and y < m and maze[x][y] == 0:
                    # keep moving in this direction
                    x += d[0]
                    y += d[1]
                # if hit the border of maze or a wall, end loop
                # [x - d[0], y - d[1]]: undo a step to get out of the wall
                # start a new search from the last valid point
                if dfs(visited, [x - d[0], y - d[1]]):
                    return True
            return False

        visited = [[0 for _ in range(m)] for _ in range(n)]
        return dfs(visited, start)
def main():
    s=Solution()
    maze1 = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start1 = [0,4]
    destination1 = [4,4]
    output1=s.hasPath(maze1,start1,destination1)
    maze2 = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start2 = [0,4]
    destination2 = [3,2]
    output2=s.hasPath(maze2,start2,destination2)
    maze3 = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]] 
    start3 = [0,4]
    destination3 = [3,2]
    output3=s.hasPath(maze3,start3,destination3)
    print("maze:",maze1,"\nstart:",start1,"\ndestination:",destination1)
    print("output:",output1)
    print()
    print("maze:",maze2,"\nstart:",start2,"\ndestination:",destination2)
    print("output:",output2)
    print()
    print("maze:",maze3,"\nstart:",start3,"\ndestination:",destination3)
    print("output:",output3)
    print()
if __name__=="__main__":
    main()
    
    





