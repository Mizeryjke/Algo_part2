class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority > other.priority


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, value, priority):
        node = Node(value, priority)
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        max_node = self.heap.pop()
        self._heapify_down(0)
        return max_node.value

    def peek(self):
        return self.heap[0].value if self.heap else None

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] < self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] < self.heap[largest]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
