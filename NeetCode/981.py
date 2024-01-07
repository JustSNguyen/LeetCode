from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map or timestamp < self.time_map[key][0][0]:
            return ""
        
        if timestamp > self.time_map[key][-1][0]:
            return self.time_map[key][-1][1]
        
        index = bisect.bisect_left(self.time_map[key], (timestamp, ""))

        if self.time_map[key][index][0] > timestamp:
            index -= 1 
        
        return self.time_map[key][index][1]

if __name__ == '__main__':
    time_map = TimeMap()
    time_map
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)