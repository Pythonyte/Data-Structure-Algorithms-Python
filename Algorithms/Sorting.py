from ADT.MaxHeap import MaxHeap

class Sorting(object):
    @staticmethod
    def heapsort(array=list):
        """
        Build a Max heap from given array
        While index:
            extract max element
            swap it with last element
            reduce size f heap by one
            now heapify the remaining heap
        :param array:
        :return: array
        """
        """
        Heap Sort Algorithm for sorting in increasing order:
            1. Build a max heap from the input data.
            2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of tree.
            3. Repeat above steps while size of heap is greater than 1.
        """
        maxheap = MaxHeap()
        maxheap.build_max_heap(array)
        while maxheap.currentsize > 0:
            maxheap.heaplist[1], maxheap.heaplist[maxheap.currentsize] = maxheap.heaplist[maxheap.currentsize], maxheap.heaplist[1]
            maxheap.currentsize -= 1
            maxheap.shift_item_down(1)
        return maxheap.heaplist