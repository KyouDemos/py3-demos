#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function

import copy
import random
import tkinter as tk
import tkinter.messagebox as msg

from adt.array import peripheryExpand
from adt.fifo_queue import FifoQueue

LIVE_CELL = '⬛'
DEAD_CELL = '⬜'


def showNote():
    print('''
    The game of Life 是由英国数学家 John H. Conway 发明的，它能模拟生物群落的兴衰更替。
    该游戏可用来观察一个复杂的系统或模式如何能从一组简单的规则演化而来。

    游戏规则
    该游戏使用一个不限大小的矩形网格，其中的每个单元格要么是空的，要么被一个有机体占据。
    被占据的单元格被视作是活的，而空的单元格被视作是死的。
    游戏的每次演进，都会基于当前的单元格布局，创造新的“一代”。

    下一代中的每个单元格状态是根据以下规则确定的：
    若某单元格是活的，并且有 2 或 3 个活的邻居，那么它在下一代也保持活。每个单元格有 8 个邻居。
    若某单元格是活的，但它没有活的邻居，或只有一个活邻居，它在下一代会死于孤立。
    一个活单元格，若有 4 个或更多个活邻居，它在下一代会死于人口过剩。
    一个死单元格，当且仅当只有 3 个活邻居时，会在下一代重生。
    用户先初始化配置，即指定哪些单元格是活的，然后运用以上的规则，生成下一代。
    可以看到，一些系统可能最终会消亡，而有些最终会进化成 “稳定” 状态。
    ''')


def letsDoIt():
    window = tk.Tk()

    text = tk.StringVar()
    text.set('')
    tk.Label(window, textvariable=text).pack(expand='yes', fill='both')

    LifeGrid().updateGrid(window, text)
    window.mainloop()


def centerWindow(window):
    """调整窗口居中"""

    window.update()

    # 窗口坐标
    # x = window.winfo_x()
    # y = window.winfo_y()

    # 窗口宽高
    w = window.winfo_width()
    h = window.winfo_height()

    # 屏幕宽高
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    # 设置屏幕坐标
    # '%dx%d+%d+%d':窗口宽x窗口高+窗口横坐标+窗口纵坐标
    window.geometry("+%d+%d" % ((sw - w) / 2, (sh - h) / 2))


class LifeGrid:
    """生物群组对象"""

    ''' 
    1. 若某单元格是活的，并且有 2 或 3 个活的邻居，那么它在下一代也保持活。每个单元格有 8 个邻居。
    2. 若某单元格是活的，但它没有活的邻居，或只有一个活邻居，它在下一代会死于孤立。
    3. 一个活单元格，若有 4 个或更多个活邻居，它在下一代会死于人口过剩。
    4. 一个死单元格，当且仅当只有 3 个活邻居时，会在下一代重生。
    '''
    RULE_DICT = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    def __init__(self, rowCnt=4, colCnt=4):

        # 使用随机值初始化二维数组
        self._grid = peripheryExpand([[random.randint(0, 1) for c in range(colCnt)] for r in range(rowCnt)], val=0)

        # 使用-1，初始化二维数组
        self._gridNew = [[-1] * len(self._grid[0]) for i in range(len(self._grid))]

        # 使用固定长度的先进先出队列保留历史状态，用于分析生命网格是否存现平衡（循环的稳定状态）
        self._history = FifoQueue(20)

    def updateCell(self, r, c):

        # 当前单元格及其所有邻居
        nbr = [self._grid[r + x][c + y] for x in (-1, 0, 1) for y in (-1, 0, 1) if
               -1 < r + x < len(self._grid) and -1 < c + y < len(self._grid[x])]

        # 根据当前单元格及其所有邻居的总人口，推算当前单元格的生存状态
        self._gridNew[r][c] = LifeGrid.RULE_DICT.get(sum(nbr))

    def updateGrid(self, window, text):

        # 保存网格历史状态，以便分析生命网格是否存现平衡（循环的稳定状态）
        self._history.add(self._gridNew)

        # 逐个推算当前单元格的生存状态
        for r in range(len(self._grid)):
            for c in range(len(self._grid[r])):
                self.updateCell(r, c)

        # 将推算结果更新到网格
        self._gridNew = peripheryExpand(self._gridNew, val=0, maxRow=50, maxCol=50)
        self._grid = copy.deepcopy(self._gridNew)

        # 鉴别异常
        if not self.isGridLive():

            msg.showinfo('运行提示', 'nothing left.')
            window.destroy()
        elif self.isGridBalance():

            msg.showinfo('运行提示', 'get balanced.')
            window.destroy()
        else:

            # 更新窗口的网格
            txt = ''
            for r in range(len(self._grid)):
                for c in range(len(self._grid[r])):
                    txt += str(self._grid[r][c])
                txt += '\n'
            text.set(txt.replace('0', DEAD_CELL).replace('1', LIVE_CELL))
            centerWindow(window)
            window.after(200, self.updateGrid, window, text)

    def isGridLive(self):
        # 计算二维数组的和
        return sum(map(sum, self._grid)) > 0

    def isGridBalance(self):
        return self._grid in self._history

    def getGrid(self):
        return self._grid


letsDoIt()
