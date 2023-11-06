import heapq

class SeatManager:
    def __init__(self, n: int):
        self.unreserved_seats_min_heap = []
        heapq.heapify(self.unreserved_seats_min_heap)
        self.marker = 1

    def reserve(self) -> int:
        if not self.unreserved_seats_min_heap:
            min_available_seat = self.marker
            self.marker += 1
            return min_available_seat

        return heapq.heappop(self.unreserved_seats_min_heap)

    def unreserve(self, seat_number: int) -> None:
        heapq.heappush(self.unreserved_seats_min_heap, seat_number)

