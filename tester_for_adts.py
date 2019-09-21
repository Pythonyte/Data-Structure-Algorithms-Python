from ADT import MinHeap, MaxHeap, Tree, BinarySearchTree
# mh = MinHeap.MinHeap()
# for i in [2,4,5,2,2,12,22]:
#     mh.insert(i)
# print(mh.heapList)
# mh1 = MinHeap.MinHeap()
# mh1.build_min_heap([2,4,5,2,2,12,22])
# print(mh1.heapList)
# mh1.display()

# array = []
# mh = MaxHeap.MaxHeap()
# for i in array:
#     mh.insert(i)
# print(mh.heaplist)
#
#
# mh1 = MaxHeap.MaxHeap()
# mh1.build_max_heap(array)
# print(mh1.heaplist)

# from Algorithms.Sorting import Sorting
#
# print(Sorting.heapsort([2,4,5,2,2,12,22]))

bst = BinarySearchTree.BinarySearchTree()
bst.set_root(84)
for item in [87,43,92,19,37,3,1,20,84]:
    bst.insert(item)
bst.print_bst()

# n1 = Tree.Node(3)
# print(n1)
