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

        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.down(0, len(self.heap))
        else:
             self.heap.pop()

        return max_value
    
    def change_priority(self, index, new_priority):
         if index < 0 or index >= len(self.heap):
            return print("Índice inválido.")
         
         old_value = self.heap[index]
         self.heap[index] = new_priority

         if new_priority > old_value:
             self.up(index)

         elif new_priority < old_value:
             self.down(index, len(self.heap))
            

    def min(self):
        if len(self.heap) == 0:
            return None

        start = (len(self.heap) - 1) // 2 + 1
        min_value = min(self.heap[start:])
        min_index = start + self.heap[start:].index(min_value)

        self.heap.pop(min_index)

        return min_value
    
    def heapsort(self):
        original = self.heap[:]
        sorted_array = []

        while self.heap:
            sorted_array.append(self.max())

        sorted_array.reverse()
        self.heap = original

        return sorted_array
    
    def get_high_priority(self):
        return self.heap[0]


heap = MaxHeap()

heap.push(5)
heap.push(3)
heap.push(17)
heap.push(10)
heap.push(84)
heap.push(19)
heap.push(6)

print("Heap após inserções:", heap.heap)
for i in range(5):
    heap.max()
    print("Heap após remoção:", heap.heap)
# heap.change_priority(2, 4)
# print('Heap depois da alteração de prioridade:', heap.heap)

# print('Elemento de maior prioridade da heap:', heap.get_high_priority())
# print('Heap reordenado:', heap.heapsort())
