from src.core.repo.data_structures.my_list.my_list_repo import ListABC, Elem


class List(ListABC):

    def find_by_data(self, data: dict) -> list[any]:
        if self.count == 0:
            raise IndexError('List is empty')
        tmp = self.head
        ans = []
        for i in range(self.count):
            if data.items() <= tmp.value.__dict__.items():
                ans.append(tmp.value)
            tmp = tmp.next
        return ans

    def __iter__(self):
        self.cur = self.head
        self.__iter = 0
        return self

    def __next__(self):
        if self.cur is None or self.__iter == self.count:
            raise StopIteration
        ans = self.cur.value
        self.__iter += 1
        self.cur = self.cur.next
        return ans

    def sort(self) -> None:
        # cocktail sort
        if self.count == 0:
            return
        left = 0
        right = self.count - 1
        while left <= right:
            for i in range(left, right):
                if self.get_elem(i).value > self.get_elem(i + 1).value:
                    self.get_elem(i).value, self.get_elem(i + 1).value = self.get_elem(i + 1).value, self.get_elem(i).value
            right -= 1
            for i in range(right, left, -1):
                if self.get_elem(i - 1).value > self.get_elem(i).value:
                    self.get_elem(i).value, self.get_elem(i - 1).value = self.get_elem(i - 1).value, self.get_elem(i).value
            left += 1

    def get_len(self):
        return self.count

    def add_tail(self, value: any) -> None:
        tmp = Elem()
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

    def print(self) -> None:
        tmp = self.head
        for i in range(self.count):
            print(tmp.value, end=' ')
            tmp = tmp.next

    def get_elem(self, position) -> Elem:
        elem = self.head
        i = 0
        while i < position:
            elem = elem.next
            i += 1
        return elem

    def remove(self, position) -> None:
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

    def del_list(self) -> None:
        while self.count != 0:
            self.remove(0)
