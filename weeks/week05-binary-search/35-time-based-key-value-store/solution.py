from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.box = {}
        self.values = {}
        self.stamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.values:
            self.values[key], self.stamp[key] = {}, []
        self.values[key][timestamp] = value
        self.stamp[key].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.stamp or timestamp < self.stamp[key][0]:
            return ""

        if not timestamp in self.values[key]:
            idx = bisect_right(self.stamp[key], timestamp)
            timestamp = self.stamp[key][min(idx-1, len(self.stamp[key])-1)]
        return self.values[key][timestamp]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)