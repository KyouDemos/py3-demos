import copy
import random
import time

from adt.fifo_queue import FifoQueue

"""
The game of Life 是由英国数学家 John H. Conway 发明的，它能模拟生物群落的兴衰更替。该游戏可用来观察一个复杂的系统或模式如何能从一组简单的规则演化而来。

游戏规则
该游戏使用一个不限大小的矩形网格，其中的每个单元格要么是空的，要么被一个有机体占据。被占据的单元格被视作是活的，而空的单元格被视作是死的。游戏的每次演进，都会基于当前的单元格布局，创造新的“一代”。下一代中的每个单元格状态是根据以下规则确定的：

若某单元格是活的，并且有 2 或 3 个活的邻居，那么它在下一代也保持活。每个单元格有 8 个邻居。
若某单元格是活的，但它没有活的邻居，或只有一个活邻居，它在下一代会死于孤立。
一个活单元格，若有 4 个或更多个活邻居，它在下一代会死于人口过剩。
一个死单元格，当且仅当只有 3 个活邻居时，会在下一代重生。
用户先初始化配置，即指定哪些单元格是活的，然后运用以上的规则，生成下一代。可以看到，一些系统可能最终会消亡，而有些最终会进化成 “稳定” 状态。
"""


class LifeGrid:
    """生物群组对象"""
    LIVE_CELL = '⬛'
    DEAD_CELL = '⬜'

    ''' 
    1. 若某单元格是活的，并且有 2 或 3 个活的邻居，那么它在下一代也保持活。每个单元格有 8 个邻居。
    2. 若某单元格是活的，但它没有活的邻居，或只有一个活邻居，它在下一代会死于孤立。
    3. 一个活单元格，若有 4 个或更多个活邻居，它在下一代会死于人口过剩。
    4. 一个死单元格，当且仅当只有 3 个活邻居时，会在下一代重生。
    '''
    RULE_DICT = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    def __init__(self, rowCnt=5, colCnt=5):
        """随机初始化网格"""

        self._grid = []
        self._history = FifoQueue(100)

        for x in range(rowCnt):
            r = []
            for y in range(colCnt):
                r.append(random.randint(0, 1))
            self._grid.append(r)

        self._gridNew = copy.deepcopy(self._grid)

    def updateCell(self, r, c):
        nbr = [self._grid[r + x][c + y] for x in (-1, 0, 1) for y in (-1, 0, 1) if
               -1 < r + x < len(self._grid) and -1 < c + y < len(self._grid[x])]
        self._gridNew[r][c] = LifeGrid.RULE_DICT.get(sum(nbr))

    def updateGrid(self):
        for r in range(len(self._grid)):
            for c in range(len(self._grid[r])):
                self.updateCell(r, c)

        self._history.add(self._grid)

        self._grid = copy.deepcopy(self._gridNew)
        self.showGrid()

    def isGridLive(self):
        return sum(map(sum, self._grid)) > 0

    def isGridBalance(self):
        return False if self._history.size == 1 else self._grid in self._history  # 此处不完美

    def showGrid(self):
        for x in range(len(self._grid)):
            for y in range(len(self._grid[x])):
                print(LifeGrid.DEAD_CELL, end='') if self._grid[x][y] == 0 else print(LifeGrid.LIVE_CELL, end='')
            print()
        print()


g = LifeGrid(6, 6)

while True:
    g.updateGrid()
    time.sleep(0.1)

    if not g.isGridLive():
        print('grid dead!')
        break
    elif g.isGridBalance():
        print("grid get balance!")
        break
