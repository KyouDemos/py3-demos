# -*- coding: utf-8 -*-
from __future__ import print_function

import copy

LIVE_CELL = '⬛'
DEAD_CELL = '⬜'


def showGrid(grid, islife=False):
    f = open('output.txt', 'a+')
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if islife:
                c = LIVE_CELL if grid[x][y] else DEAD_CELL
            else:
                c = str(grid[x][y])
            print(c, end='', file=f)
        print(file=f)
    print(file=f)
    f.close()


def peripheryExpand(grid, val=None, maxRow=100, maxCol=100):
    """保证网格四周的行列的值全部为0"""

    sTop = sum([grid[0][c] for c in range(len(grid[0]))])
    if sTop > 0 and len(grid) < maxRow:
        zero = [[val] * len(grid[0])]
        zero.extend(grid)
        grid = copy.deepcopy(zero)

    sDown = sum([grid[-1][c] for c in range(len(grid[-1]))])
    if sDown > 0 and len(grid) < maxRow:
        grid.extend([[0] * len(grid[-1])])

    sLeft = sum([grid[r][0] for r in range(len(grid))])
    if sLeft > 0:
        for r in range(len(grid)):
            if len(grid[r]) < maxCol:
                zero = [0]
                zero.extend(grid[r])
                grid[r] = zero

    sRight = sum([grid[r][-1] for r in range(len(grid))])
    if sRight > 0:
        for r in range(len(grid)):
            if len(grid[r]) < maxCol:
                grid[r].append(0)

    return grid
