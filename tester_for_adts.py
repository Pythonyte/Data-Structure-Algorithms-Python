from ADT import MinHeap
mh = MinHeap.MinHeap()
mh.insert(2)
mh.insert(4)
mh.insert(5)
mh.insert(2)
mh.insert(2)
mh.insert(12)
mh.insert(22)
print(mh.heapList)
mh.remove()
mh.remove()
mh.remove()
print(mh.heapList)