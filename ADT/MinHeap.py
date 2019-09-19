class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def shift_item_up(self, index):
        """
        Regain heap property after appending new element in heaplist
        shift item upside untill its parent is greater than element.
        parent of index : index // 2
        :param index:
        :return:
        """
        parent_index = index // 2

        # check if parent index exists
        while parent_index > 0:

            # swap if element is smaller than parent
            if self.heapList[index] < self.heapList[parent_index]:
                self.heapList[parent_index], self.heapList[index] = self.heapList[index], self.heapList[parent_index]

            # shift up index to one level and continue checking for more top levels
            parent_index = parent_index // 2

    def smallest_child_index(self, parent_index):
        left_child_index = 2 * parent_index
        right_child_index = 2 * parent_index + 1

        # if heaplist is lesser than left_child_index, means no child exists for that parent
        if self.currentSize < left_child_index:
            return -1

        # if heaplist is lesser than right_child_index, means left chlid is smallest
        if self.currentSize < right_child_index:
            return left_child_index

        # if both childs exists then figure out minimum one
        if self.heapList[left_child_index] < self.heapList[right_child_index]:
            return left_child_index
        else:
            return right_child_index

    def shift_item_down(self, index):
        """
        Come down from top to bottom and re-establish the heap-order-property
        if parent is greater than childs, then replace it with smallest child and do that action
        again for next level
        :param index:
        :return:
        """
        while index * 2 <= self.currentSize:
            child_index = self.smallest_child_index(index)

            # swap if element is larger than child
            if self.heapList[index] > self.heapList[child_index]:
                self.heapList[child_index], self.heapList[index] = self.heapList[index], self.heapList[child_index]

            # check this again for same item.. which is now at child_index position
            index = child_index

    def insert(self, value):
        """
        Add item in list
        increment count
        shift item up to maintain heap properties
        :param value:
        :return:
        """
        self.heapList.append(value)
        self.currentSize += 1
        self.shift_item_up(self.currentSize)


    def remove(self):
        ######
        ## We are replacing item at index=1 bcoz to achieve heap structure property, we ignored 0th index of heaplist
        min_value = self.heapList[1]

        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()

        self.shift_item_down(1)
        return min_value

    def build_min_heap(self, heaplist):
        """
        Go to the last non-leaf node, i.e. total size //2
        because its a complete binary tree

        for each non-leaf node starting from last to root,
        use shift item down to establish heap-order property for node.
        complexity O(n)
        explanation: https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/

        :param heaplist:
        :return:
        """
        if not heaplist:
            return -1

        self.heapList += heaplist
        self.currentSize += len(heaplist)
        index = self.currentSize // 2

        while index > 0:
            self.shift_item_down(index)
            index -= 1

    def display(self):
        level_end = 1

        for index, value in enumerate(self.heapList):
            if index == 0:
                continue

            print(value, end=" ", sep=" ")
            if index == level_end:
                print("\n")
                level_end = max(level_end, 2*index + 1)
