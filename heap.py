class MaxHeap:

    def __init__(self):
        self.heap = []

    def up(self, i):
    
        j = (i - 1) // 2

        if j > 1:
            if self.heap[j] < self.heap[i]:
                self.heap[j], self.heap[i] = self.heap[i], self.heap[j]
                self.up(j)
        
    def down(self, i):

        j = 2 * i + 1

        if j < n:
            
