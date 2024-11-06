class MaxHeap:

    def __init__(self):
        self.heap = []

    def up(self, i):
        j = (i - 1) // 2

        if j >= 0 and self.heap[j] < self.heap[i]:
                self.heap[j], self.heap[i] = self.heap[i], self.heap[j]
                self.up(j)

    def down(self, i, n):
        j = 2 * i + 1

        if j < n:
            if j + 1 < n and self.heap[j + 1] > self.heap[j]:
                j += 1

            if self.heap[i] < self.heap[j]:
                    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                    self.down(j, n)

    def push(self, value):
        self.heap.append(value)
        self.up(len(self.heap) - 1)

    def max(self):
        if len(self.heap) == 0:
            return None

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.down(0, len(self.heap))
        return max_value


heap = MaxHeap()

heap.push(10)
heap.push(20)
heap.push(30)

print("Heap após inserções:", heap.heap)


print("Maior elemento extraído:", heap.max())
print("Heap após extração:", heap.heap)

