import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) < len(self.min_heap):
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -value)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            median1 = self.min_heap[0]
            median2 = -self.max_heap[0]
            return (median1 + median2) / 2

        return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == '__main__':
    md = MedianFinder()

    md.addNum(-1)
    md.findMedian()
    md.addNum(-2)
    md.findMedian()
    md.addNum(-3)
    md.findMedian()
    md.addNum(-4)
    md.findMedian()
    md.addNum(-5)
    md.findMedian()
