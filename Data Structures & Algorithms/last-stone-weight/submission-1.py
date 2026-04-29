class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a maxheap by mutliplying all the stones by -1 
        maxHeap = [-s for s in stones] 
        heapq.heapify(maxHeap)

        
        while len(maxHeap) >= 2: 

            y = -heapq.heappop(maxHeap) 
            x = -heapq.heappop(maxHeap) 

            if y > x: 
                heapq.heappush(maxHeap, x-y)

        return -heapq.heappop(maxHeap) if maxHeap else 0 
