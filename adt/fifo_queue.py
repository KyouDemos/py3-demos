# -*- coding: utf-8 -*-
import copy


class FifoQueue:
    """先进先出、定长队列"""

    def __init__(self, size=10, maxHead=10):
        """队列初始化、默认长度：10"""
        self._queue = []
        self._head = 0
        self._size = size
        self._maxHead = maxHead

    def add(self, item):
        self._queue.append(copy.deepcopy(item))
        if len(self._queue) > self._size:
            self._head += 1
            self.clean()

    def clean(self):
        """避免队列过长或频繁截断数组"""
        if self._head > self._maxHead:
            self._queue = self._queue[self._head:]
            self._head = 0

    def __contains__(self, item):
        return item in self._queue[self._head:]

    def getQueue(self):
        return self._queue
