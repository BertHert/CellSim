import pygame

rect = pygame.Rect(0, 0 , 5, 5)

cols = 5
rows = 5

arr =[[0]*cols]*rows
arr = [[0 for i in range(cols)] for j in range(rows)]

for row in range(len(arr)-1):
    for col in range(len(arr[row])-1):
        arr[row][col] = 1


for row in arr:
    print(row)

