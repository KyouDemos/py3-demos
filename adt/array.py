# -*- coding: utf-8 -*-
from __future__ import print_function

import copy


# TODO 只能扩展，不能收缩，不完美。
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
