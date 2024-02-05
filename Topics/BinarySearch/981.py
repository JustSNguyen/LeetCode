from collections import defaultdict
import bisect
class TimeMap:
    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.values[key] or timestamp < self.values[key][0][0]:
            return ""

        if timestamp > self.values[key][-1][0]:
            return self.values[key][-1][1]

        j = bisect.bisect_left(self.values[key], (timestamp, ""))
        if self.values[key][j][0] == timestamp:
            return self.values[key][j][1]

        return self.values[key][j - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)