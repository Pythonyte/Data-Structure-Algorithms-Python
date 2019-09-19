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
            index = parent_index

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
        pass