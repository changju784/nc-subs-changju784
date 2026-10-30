import heapq

class SeatManager:
    def __init__(self, n: int):
        self.total_seats = n
        self.availables = [i for i in range(1, n+1)]
        self.occupied = set() 

    def reserve(self) -> int:
        reserved = heapq.heappop(self.availables)
        self.occupied.add(reserved)
        return reserved
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.availables, seatNumber)
        self.occupied.remove(seatNumber)
        return 
        
