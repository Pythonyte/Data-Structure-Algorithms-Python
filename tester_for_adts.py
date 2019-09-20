from ADT import MinHeap, MaxHeap
# mh = MinHeap.MinHeap()
# for i in [2,4,5,2,2,12,22]:
#     mh.insert(i)
# print(mh.heapList)
# mh1 = MinHeap.MinHeap()
# mh1.build_min_heap([2,4,5,2,2,12,22])
# print(mh1.heapList)
# mh1.display()

array = [2,4,5,22,34]
mh = MaxHeap.MaxHeap()
for i in array:
    mh.insert(i)
print(mh.heaplist)


mh1 = MaxHeap.MaxHeap()
mh1.build_max_heap(array)
print(mh1.heaplist)