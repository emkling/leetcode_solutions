class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or newColor == image[sr][sc]:
            return image
        
        self.fill(sr, sc, newColor, image, image[sr][sc])
        return image
        
    def fill(self, row, column, newColor, image, initialColor):
        if row < 0 or row > len(image)-1 or column < 0 or column > len(image[0])-1 or initialColor != image[row][column]:
            return 
        
        image[row][column] = newColor
        
        self.fill(row+1, column, newColor, image, initialColor)
        self.fill(row-1, column, newColor, image, initialColor)
        self.fill(row, column+1, newColor, image, initialColor)
        self.fill(row, column-1, newColor, image, initialColor)
        
        