def flood_fill(image, limy, limx, oldColor, newColor, y, x ):
    image[y][x] = newColor

    if y + 1 < limy and image[y+1][x] == oldColor:
        flood_fill(image, limy, limx, oldColor, newColor, y+1, x)
    
    if y - 1 >= 0 and image[y-1][x] == oldColor:
        flood_fill(image, limy, limx, oldColor, newColor, y-1, x)
    
    if x + 1 < limx and image[y][x + 1] == oldColor:
        flood_fill(image, limy, limx, oldColor, newColor, y, x+1)
    
    if x - 1 >= 0 and image[y][x - 1] == oldColor:
        flood_fill(image, limy, limx, oldColor, newColor, y, x-1)
    
    return


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        oldColor = image[sr][sc]
        limy = len(image)
        limx = len(image[0])

        if oldColor == newColor:
            return image
        
        flood_fill(image, limy, limx, oldColor, newColor, sr, sc)

        return image