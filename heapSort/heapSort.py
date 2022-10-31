class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)

def heapify(queue,i, m):
    right = 2*i + 1
    left = 2*i + 2
    maxValIndex = i
    if (right <= m) and (queue.items[right] > queue.items[maxValIndex]):
        maxValIndex = right
    if (left <= m) and (queue.items[left] > queue.items[maxValIndex]):
        maxValIndex = left
    
    if maxValIndex != i:
        queue.items[maxValIndex], queue.items[i] = queue.items[i], queue.items[maxValIndex]
        heapify(queue, maxValIndex, m)

def BuildHeap(queue, n):
    for i in range(n//2, 0, -1):
        heapify(queue, i, n)

def heapSort(queue, n):
    k = n
    BuildHeap(queue, k)
    m = n
    while(m > 0):
        queue.items[0], queue.items[m] = queue.items[m], queue.items[0]
        m -= 1
        heapify(queue, 0, m)

q = Queue()
lis = [87, 57, 44, 12, 15, 19, 23]
for i in lis:
    q.enqueue(i)

print(q.items)
heapSort(q, len(q.items)-1)
print("After sort", q.items)



