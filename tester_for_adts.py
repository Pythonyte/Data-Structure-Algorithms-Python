from ADT import MinHeap
mh = MinHeap.MinHeap()
for i in [2,4,5,2,2,12,22]:
    mh.insert(i)
print(mh.heapList)
mh1 = MinHeap.MinHeap()
mh1.build_min_heap([2,4,5,2,2,12,22])
print(mh1.heapList)
mh1.display()