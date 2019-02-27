class FifoQueue:
    """先进先出、定长队列"""

    MAX_HEAD = 10

    def __init__(self, size=10):
        """队列初始化、默认长度：10"""
        self._queue = []
        self._head = 0
        self.size = size

    def add(self, item):
        self._queue.append(item)
        if len(self._queue) > self.size:
            self._head += 1

            # 避免队列过长或频繁截断数组
            self.clean()

    def clean(self):
        if self._head > FifoQueue.MAX_HEAD:
            self._queue = self._queue[self._head:]
            self._head = 0

    def __contains__(self, item):
        return item in self._queue[self._head:]
