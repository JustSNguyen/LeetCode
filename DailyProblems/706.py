class MyHashMap:
    NOT_TAKEN = 0
    TAKEN = 1
    REMOVED = 2
    MAX_SIZE = 1000005

    def __init__(self):
        self.status = [MyHashMap.NOT_TAKEN for _ in range(MyHashMap.MAX_SIZE)]
        self.value = [0 for _ in range(MyHashMap.MAX_SIZE)]

    def put(self, key: int, value: int) -> None:
        self.value[key] = value
        self.status[key] = MyHashMap.TAKEN

    def get(self, key: int) -> int:
        if self.status[key] != MyHashMap.TAKEN:
            return -1
        return self.value[key]

    def remove(self, key: int) -> None:
        self.status[key] = MyHashMap.REMOVED
