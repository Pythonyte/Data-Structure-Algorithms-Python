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

    def max_child_index(self, parent_index):
        left_child_index = 2 * parent_index
        right_child_index = 2 * parent_index + 1

        # if heaplist is lesser than left_child_index, means no child exists for that parent
        if self.currentsize < left_child_index:
            return -1

        # if heaplist is lesser than right_child_index, means left chlid is smallest
        if self.currentsize < right_child_index:
            return left_child_index

        # if both childs exists then figure out maximum one
        if self.heaplist[left_child_index] < self.heaplist[right_child_index]:
            return right_child_index
        else:
            return left_child_index

    def shift_item_down(self, parent_index):
        """
        get child index having maximum value
        if max child is greater than parent, it should be on the top... Move it by swapping
        Do the same... untill reach to leaf node
        :param parent_index:
        :return:
        """
        while 2 * parent_index <= self.currentsize:
            child_index = self.max_child_index(parent_index)
            if self.heaplist[child_index] > self.heaplist[parent_index]:
                self.heaplist[child_index], self.heaplist[parent_index] = self.heaplist[parent_index], self.heaplist[child_index]
            parent_index = child_index

    def remove(self):
        """
            Remove top item, which is max of heap
            put last element at the top
            shift items down untill leaf
        """
        max_item = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize -= 1
        self.heaplist.pop()
        self.shift_item_down(1)
        return max_item

    def build_max_heap(self, list_to_be_heap):
        """
        Fill heap with given list
        shift items down, but in reverse order
        to optimize: start from last non leaf node to top
        :param list_to_be_heap:
        :return:
        """
        self.heaplist = self.heaplist + list_to_be_heap
        self.currentsize = len(list_to_be_heap)

        # as it follow properties of complete binary tree, non leaf nodes will end to total size / 2
        index = self.currentsize // 2

        # > 0 : to ignore first element of the array which is 0..
        while index > 0:
            self.shift_item_down(index)
            index -= 1
