from collections import deque
class Solution:
    def hasPath(self, maze, start,destination) -> bool:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        N = len(maze)
        M = len(maze[0])
        
        queue = deque()
        eRow, eCol = start
        queue.append((eRow, eCol))
        visited = set((eRow, eCol))
        
        
        while queue:
            row, col = queue.popleft()
            if [row, col] == destination:
                return True
            
            for (rowOffset, colOffset) in directions:
                r = row + rowOffset
                c = col + colOffset
                while 0 <= r <= N -1 and 0 <= c <= M - 1 and maze[r][c] == 0:
                    r += rowOffset 
                    c += colOffset
                    
                new_r, new_c = r - rowOffset, c - colOffset
                if (new_r, new_c) not in visited:
                    queue.append((new_r, new_c))
                    visited.add((new_r, new_c))
            
        return False
        
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
    print("maze:",maze2,"\nstart:",start2,"\ndestination:",destination2)
    print("output:",output2)
    print("maze:",maze3,"\nstart:",start3,"\ndestination:",destination3)
    print("output:",output3)
if __name__=="__main__":
    main()
    
    
