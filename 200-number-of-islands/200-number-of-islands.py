class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0 
        
        for rows in range(len(grid)):
            for cols in range(len(grid[0])):
                if grid[rows][cols] == '1':
                    self.dfs(grid, rows, cols)
                    count += 1
                    
        
        return count
    
    
    def dfs(self, grid, r, c):
    
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
            return

        grid[r][c] = '#'

        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)