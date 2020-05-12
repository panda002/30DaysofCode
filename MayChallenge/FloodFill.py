def floodfill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return
    callDfs(image,sr, sc, image[sr][sc], newColor)
    return image


def callDfs(image, sr, sc, oldColor, newColor):
    if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != oldColor:
        return
    image[sr][sc] = newColor
    callDfs(image, sr + 1, sc, oldColor, newColor)  # if 1,1 it will go to 2,1 down
    callDfs(image, sr - 1, sc, oldColor, newColor)  # if 1,1 it will go to 0,1 up
    callDfs(image, sr, sc + 1, oldColor, newColor)  # if 1,1 it will go to 1,2 right
    callDfs(image, sr, sc - 1, oldColor, newColor)  # if 1,1 it will go to 1,0 left


print(floodfill([[1, 1, 1],
                [1, 1, 0],
                [1, 0, 1]],
                1, 1, 2))
