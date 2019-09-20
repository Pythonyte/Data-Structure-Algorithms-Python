class MaxHeap:
    """
        Features of MinHeap:
            insert
            remove
            build_max_heap
            get_max
            display
    """
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def shift_item_up(self, index):
        """
        As its maxheap, max element should be in top.
        We have to traverse from last element to upside and swap if parent is greater.. till we come to root
        :param index:
        :return:
        """
        while index > 0:
            parent_index = index // 2
            if parent_index > 0 and self.heaplist[parent_index] < self.heaplist[index]:
                self.heaplist[parent_index], self.heaplist[index] = self.heaplist[index], self.heaplist[parent_index]
            index = index // 2

    def insert(self, item):
        """
        Insert a new element into last
        start shifting item upside
        :param item:
        :return:
        """
        self.heaplist.append(item)
        self.currentsize += 1
        self.shift_item_up(self.currentsize)

    def shift_item_down(self, index):
        pass
    
    def remove(self):
        """
            Remove top item, which is max of heap
            put last element at the top
            shift items down untill leaf
        """
        max_item = self.heaplist[1]
        self.heaplist = [0] + self.heaplist[2:]
        self.currentsize -= 1
        self.shift_item_down(1)
        return max_item

