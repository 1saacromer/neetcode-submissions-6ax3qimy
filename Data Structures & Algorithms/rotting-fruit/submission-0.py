class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        maxHeight = len(grid)
        maxWidth = len(grid[0])
        directions = [[-1, 0], [1,0], [0, -1], [0, 1]] 
        q = deque()
        
        total = 0

        for i in range(maxHeight): 
            for j in range(maxWidth): 
                if grid[i][j] == 2: 
                    q.append((i, j))

        toProcess = len(q)
        while q: 
            node = q.popleft() 
            toProcess -= 1
            
            row = node[0]
            col = node[1]

            for dy, dx in directions: 
                nrow = row + dy 
                ncol = col + dx

                if 0 <= nrow < maxHeight and 0 <= ncol < maxWidth and grid[nrow][ncol] == 1:   
                    grid[nrow][ncol] = 2
                    q.append((nrow, ncol))
            grid[row][col] = 0
            print(q)
            if not toProcess and q: 
                total += 1 
                toProcess = len(q)
            



        print(grid)
        res = all(x == 0 for row in grid for x in row)
        if not res:
            return -1 
        return total

        