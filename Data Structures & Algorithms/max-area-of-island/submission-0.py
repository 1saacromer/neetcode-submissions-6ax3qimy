class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        max_area = 0

        def dfs(i, j): 
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0: 
                return 0
            
            area = 1
            grid[i][j] = 0
            for di, dj in directions: 
                area += dfs(i + di, j + dj) 
            
            print(area)
            return area
            
        


        for i in range(ROWS): 
            for j in range(COLS): 
                if grid[i][j] == 1: 
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        

        return max_area 