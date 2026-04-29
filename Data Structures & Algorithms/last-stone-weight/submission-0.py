class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a maxheap by mutliplying all the stones by -1 
        maxHeap = [] 
        for stone in stones: 
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) >= 2: 
            y = -heapq.heappop(maxHeap) 
            x = -heapq.heappop(maxHeap) 

            if y > x: 
                y -= x 
                heapq.heappush(maxHeap, -y)

        return -heapq.heappop(maxHeap) if maxHeap else 0 
