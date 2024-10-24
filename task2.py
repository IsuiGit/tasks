import time
from collections import deque

class ListFIFO:
    def __init__(self):
        self.q = []

    def printData(self):
        for i in self.q:
            print(i)

    def appendData(self, data):
        self.q.append(data)

    def popData(self):
        if len(self.q)>0:
            self.q.pop(i)
        else:
            return 'List is empty'

class DequeFIFO:
    def __init__(self):
        self.q = deque()

    def printData(self):
        for i in self.q:
            print(i)

    def appendData(self, data):
        self.q.append(data)

    def popData(self):
        if len(self.q)>0:
            self.q.popleft()
        else:
            return 'List is empty'

#ListFIFO test
start = time.monotonic_ns()
queue = ListFIFO()
for i in range(2**8):
    queue.appendData(i)
queue.printData()
for i in range(100):
    queue.popData()
queue.printData()
finish = time.monotonic_ns()
print(f'Время работы ListFIFO: {finish - start}')

#DequeFIFO test
start = time.monotonic_ns()
queue = DequeFIFO()
for i in range(2**8):
    queue.appendData(i)
queue.printData()
for i in range(100):
    queue.popData()
queue.printData()
finish = time.monotonic_ns()
print(f'Время работы DequeFIFO: {finish - start}')
