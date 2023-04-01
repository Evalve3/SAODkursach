class Elem:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def get_len(self):
        return self.count

    def add_tail(self, value=None):
        tmp = Elem()
        if value is None:
            value = int(input())
        if self.count == 0:
            self.head = self.tail = tmp
            tmp.next = tmp
            tmp.prev = tmp
        else:
            self.tail.next = tmp
            self.head.prev = tmp
            tmp.prev = self.tail
            self.tail = tmp
            tmp.next = self.head
        tmp.value = value
        self.count += 1

    def show_list(self):
        tmp = self.head
        for i in range(self.count):
            print(tmp.value, end=' ')
            tmp = tmp.next

    def get_elem(self, position):
        elem = self.head
        i = 0
        while i < position:
            elem = elem.next
            i += 1
        return elem

    def del_elem(self, position):
        if self.count == 0:
            raise IndexError('List is empty')
        if position >= self.count or position < 0:
            raise IndexError('Index out of range')
        del_node = self.get_elem(position)
        if self.count != 1:
            prev_node = del_node.prev
            after_node = del_node.next
            prev_node.next = after_node
            after_node.prev = prev_node
            if position == 0:
                self.head = after_node
            elif position == self.count - 1:
                self.tail = prev_node
        else:
            self.head = None
            self.tail = None
        del del_node
        self.count -= 1

    def del_list(self):
        while self.count != 0:
            self.del_elem(0)
