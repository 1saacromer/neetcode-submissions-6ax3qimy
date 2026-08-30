class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue 
                count += 1
                self.dfs(i, j, grid)
            
        
        return count 
                
    def dfs(self, i, j, grid):
        if i < 0 or j < 0 or j > len(grid[0]) - 1 or i > len(grid) - 1 or grid[i][j] == '0': 
            return 

        grid[i][j] = '0'
        uy, dy = i - 1, i + 1 
        rx, lx = j + 1, j - 1 

        self.dfs(uy, j, grid) 
        self.dfs(dy, j, grid)
        self.dfs(i, rx, grid)
        self.dfs(i, lx, grid)






        