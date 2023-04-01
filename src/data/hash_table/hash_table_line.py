import re
import random
import math

from src.core.hash_table.hash_table_repo import HashTableABC

table_len = 100


class HashTableLine(HashTableABC):
    KEY_LEN = 6
    MAX_K = 30
    C, D = 1, 1

    @staticmethod
    def is_key(key) -> bool:
        r = re.compile(r"^[A-Z][0-9]{3}[A-Z]{2}$")
        return r.match(key) is not None

    def hash(self, key) -> int:
        hash_value = 5381
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % table_len

    def insert(self, key: str) -> None:
        k = 0
        if not self.is_key(key):
            print("Incorrect key")
            return
        i = -1
        while True:
            i += 1
            id = (self.hash(key) + self.C * i + self.D * i + k) % table_len
            k += 1
            if k > self.MAX_K:
                return

            if self.dict[id].key == key:
                self.dict[id].key = key
                return

            if not self.dict[id].key:
                self.dict[id].key = key
                return

    def find(self, key: str) -> int:
        if not self.is_key(key):
            print("Incorrect key")
            return -1
        k = 0
        i = -1
        while True:
            i += 1
            id = (self.hash(key) + self.C * i + self.D * i + k) % table_len
            if not self.dict[id].deleted and not self.dict[id].key:
                return -1
            k += 1
            if k > self.MAX_K:
                return -1
            if self.dict[id].key == key:
                return id

    def find_by_index(self, index) -> str:
        if index >= table_len:
            print("Incorrect index")
            return ""
        if not self.dict[index].key:
            return ""
        return self.dict[index].key

    def print(self) -> None:
        for i in range(table_len):
            if self.dict[i].key:
                print(self.dict[i].key, i, end=' ')
        print()

    def remove(self, key: str) -> None:
        if not self.is_key(key):
            print("Incorrect key")
            return
        id = self.find(key)
        if id != -1:
            self.dict[id].deleted = True
            self.dict[id].key = ""

    def fill_table(self) -> None:
        key = '123456'
        # (r"^[A-Z][0-9]{3}[A-Z]{2}$")
        for i in range(table_len * 10):
            for j in range(self.KEY_LEN):
                if j in (1, 2, 3):
                    key = key[:j] + str(random.randint(0, 9)) + key[j+1:]
                else:
                    key = key[:j] + chr(random.randint(ord('A'), ord('Z'))) + key[j+1:]
            self.insert(key)

