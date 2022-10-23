# A Python program for Prims's MST for
# adjacency list representation of graph

from collections import defaultdict
import math


class Heap():

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def new_heap_node(self, v, dist):
        heapNode = [v, dist]
        return heapNode

    # A utility function to swap two nodes of
    # min heap. Needed for min heapify
    def swap_heap_node(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    # A standard function to heapify at given idx
    # This function also updates position of nodes
    # when they are swapped. Position is needed
    # for decreaseKey()
    def heapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        # The nodes to be swapped in min heap
        # if idx is not smallest
        if smallest != idx:
            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            # Swap nodes
            self.swap_heap_node(smallest, idx)
            self.heapify(smallest)

    # Standard function to extract minimum node from heap
    def extract_minimum(self):

        # Return NULL wif heap is empty
        if self.isEmpty() == True:
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.heapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):

        # Get the index of v in heap array

        i = self.pos[v]

        # Get the node and update its dist value
        self.array[i][1] = dist

        # Travel up while the complete tree is not
        # hepified. This is a O(Logn) loop
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:
            # Swap this node with its parent
            self.pos[self.array[i][0]] = (i - 1) / 2
            self.pos[self.array[(i - 1) // 2][0]] = i
            self.swap_heap_node(i, (i - 1) // 2)

            # move to parent index
            i = (i - 1) // 2

    # A utility function to check if a given vertex
    # 'v' is in min heap or not
    def isInheap(self, v):

        if self.pos[v] < self.size:
            return True
        return False


def printArr(graph, parent, n):
    w_sum = 0
    for i in range(1, n):
        # print("% d - % d" % (parent[i], i))
        for j in graph[parent[i]]:
            if j[0] == i:
                w_sum += j[1]
    print(str(abs(w_sum)))


def PrimMST(graph, n):
    # Get the number of vertices in graph
    V = n

    # key values used to pick minimum weight edge in cut
    key = []

    # List to store constructed MST
    parent = []

    # heap represents set E
    heap = Heap()

    # Initialize min heap with all vertices. Key values of all
    # vertices (except the 0th vertex) is initially infinite
    for v in range(V):
        parent.append(-1)
        key.append(math.inf)
        heap.array.append(heap.new_heap_node(v, key[v]))
        heap.pos.append(v)

    # Make key value of 0th vertex as 0 so
    # that it is extracted first
    heap.pos[0] = 0
    key[0] = 0
    heap.decreaseKey(0, key[0])

    # Initially size of min heap is equal to V
    heap.size = V

    # In the following loop, min heap contains all nodes
    # not yet added in the MST.
    while heap.isEmpty() == False:

        # Extract the vertex with minimum distance value
        new_heap_node = heap.extract_minimum()
        u = new_heap_node[0]

        # Traverse through all adjacent vertices of u
        # (the extracted vertex) and update their
        # distance values
        for pCrawl in graph[u]:

            v = pCrawl[0]

            # If shortest distance to v is not finalized
            # yet, and distance to v through u is less than
            # its previously calculated distance
            if heap.isInheap(v) and pCrawl[1] < key[v]:
                key[v] = pCrawl[1]
                parent[v] = u

                # update distance value in min heap also
                heap.decreaseKey(v, key[v])

    printArr(graph, parent, V)


def read_graph():
    graph = defaultdict(list)
    n, m = map(int, input().split(" "))
    for i in range(n):
        u, v, w = map(int, input().split(" "))
        graph[u - 1].append([v - 1, w * -1])
        graph[v - 1].append([u - 1, w * -1])

    return graph, n


if __name__ == '__main__':
    # Driver program to test the above functions

    graph, n = read_graph()

    '''
    # Не работает с дублирующими ребрами
    graph = Graph(3)
    graph.addEdge(0, 1, 1)
    graph.addEdge(0, 1, 2)
    graph.addEdge(1, 2, 1)
    '''

    # graph = Graph(2)

    PrimMST(graph, n)

# This code is contributed by Divyanshu Mehta
