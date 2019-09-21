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
bst.set_root(10)
for item in [5,6,7,8]:
    bst.insert(item)
bst.print_bst()
import pdb;pdb.set_trace()
# n1 = Tree.Node(3)
# print(n1)
