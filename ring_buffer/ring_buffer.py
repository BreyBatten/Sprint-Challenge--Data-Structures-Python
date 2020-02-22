from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if there's room in the buffer, add new item to tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # if there's not room, remove the head and add the tail
        elif self.storage.length == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        if self.storage.head:
            list_buffer_contents.append(self.storage.head.value)
            current_node = self.storage.head

            for i in range(self.storage.length - 1):
                list_buffer_contents.append(current_node.next.value)
                current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
