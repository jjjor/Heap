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


    def build_heap(self, array):
        self.heap = array

        for i in range(len(array) // 2, -1, -1):
            self.down(i, len(array))

    def display_heap(self):
        print('Heap atual:', self.heap)

heap = MaxHeap()


# Conjunto 1 ---------------------------------------------------------------------------------

heap.heap = [10, 5, 20, 1, 15, 30, 25]  

heap.build_heap(heap.heap)
heap.display_heap()

heap.change_priority(3, 50)

print('Heap após mudança de prioridade: ', heap.heap)

heap.change_priority(1, 8)

print('Heap após mudança de prioridade: ', heap.heap)

for i in range(3):
    heap.max()
    print('Heap após remoção: ', heap.heap)

print('Heapsort: ', heap.heapsort())

print('High priority:', heap.get_high_priority())

# Conjunto 2 ---------------------------------------------------------------------------------
print('CONJUNTO 2')
heap.heap = []

heap.push(1)
heap.push(2)
heap.push(3)
heap.push(4)
heap.push(5)
heap.push(6)
heap.push(7)
heap.push(8)
heap.push(9)
heap.push(10)

heap.display_heap()

heap.change_priority(4, 15)
heap.change_priority(8, 3)

print('Heap após mudança de prioridade: ', heap.heap)

for i in range(5):
    heap.max()
    print('Heap após remoção: ', heap.heap)

print('Heap após ordenação: ', heap.heapsort())

print('High priority:', heap.get_high_priority())

# Conjunto 3 ---------------------------------------------------------------------------------
print('CONJUNTO 3')
heap.heap = []

heap.push(50)
heap.push(40)
heap.push(30)
heap.push(20)
heap.push(10)
heap.push(5)
heap.push(3)

heap.display_heap()

heap.change_priority(2, 60)

print('Heap após mudança de prioridade: ', heap.heap)

heap.change_priority(5, 1)

print('Heap após mudança de prioridade: ', heap.heap)

for i in range(3):
    heap.max()
    print('Heap após remoção: ', heap.heap)

print('Heap após ordenação: ', heap.heapsort())

print('High priority:', heap.get_high_priority())

# Conjunto 4 ---------------------------------------------------------------------------------

print('CONJUNTO 4')
heap.heap = []

heap.push(13)
heap.push(26)
heap.push(19)
heap.push(17)
heap.push(24)
heap.push(31)
heap.push(22)
heap.push(11)
heap.push(8)
heap.push(20)
heap.push(5)
heap.push(27)
heap.push(18)

heap.display_heap()

heap.change_priority(7, 35)

print('Heap após mudança de prioridade: ', heap.heap)

heap.change_priority(10, 12)

print('Heap após mudança de prioridade: ', heap.heap)

for i in range(4):
    heap.max()
    print('Heap após remoção: ', heap.heap)

print('Heap após ordenação: ', heap.heapsort())

print('High priority:', heap.get_high_priority())


