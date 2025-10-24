from collections import deque, OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.box = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.box:
            return -1
        self.box.move_to_end(key)        
        return self.box[key]

    def put(self, key: int, value: int) -> None:
        if key in self.box:
            self.box.move_to_end(key)
        self.box[key] = value
        if len(self.box) > self.capacity:
            self.box.popitem(last=False)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)