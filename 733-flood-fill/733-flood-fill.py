class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image == None or image[sr][sc] == newColor:
            return image
        
        self.fill(sr, sc, image, image[sr][sc], newColor)
        return image
        
    def fill(self, r, c, image, initial, newColor):
        if r < 0 or r > len(image) -1 or c < 0 or c > len(image[0])-1 or initial != image[r][c]:
            return
        image[r][c] = newColor
            
        self.fill(r+1, c, image, initial, newColor)
        self.fill(r-1, c, image, initial, newColor)
        self.fill(r, c+1, image, initial, newColor)
        self.fill(r, c-1, image, initial, newColor)
    