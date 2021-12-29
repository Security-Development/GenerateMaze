from random import *

size = int(input('Input MazeSize: ')) # 홀수
interval = int(input('Input MazeInterval: '))# 짝수
array = []

def mazeInit(size):

    global array, interval

    array = [[0 for col in range(size)] for row in range(size)]

    for y in range(size):
        for x in range(size):
            if x == 0 or x == size -1 or y == 0 or y == size -1:
                array[y][x] = '■ '
                continue
            if x % (interval) == 0 and y % (interval) == 0:
                array[y][x] = '■ '
            else:
                array[y][x] = '□ '

def addInterval(type, y, x):
    global array, interval

    if type == 1:
        for i in range(interval -1):
            array[(y+1) + (i)][x] = '■ '
    elif type == 2:
        for i in range(interval):
            array[y][(x+1) + (i)] = '■ '
    elif type == 3:
        for i in range(interval -1):
            array[(y-1) - (i)][x] = '■ '

def generateMaze():
    global array, interval
    for y in range(size):
        for x in range(size):
            if x % 3 == 0 and y % 3 == 0 and x < (size - 3) and y < (size - 3):
                rand = randint(1,3)
                #print(f'x => {x}, y => {y}\n')
                addInterval(rand, y, x)
                    

                


def printMaze():
    for y in range(size):
        for x in range(size):
            print(array[y][x], end='')
        print()

mazeInit(size) # 홀수 입력
generateMaze()
printMaze()


