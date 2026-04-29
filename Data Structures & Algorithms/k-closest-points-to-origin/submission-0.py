class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [] 

        for p in points: 

            # calculate the distance 
            d = p[0] ** 2 + p[1] ** 2

            # if the distance of the current point is closer, add it to the heap
            ini = (-d, p[0], p[1]) 
            heapq.heappush(maxHeap, ini)

            # only remove from the heap if it has more than k points in it 
            if len(maxHeap) > k: 
                heapq.heappop(maxHeap)
        
        # ensure the return type is a list of lists of integer pairs that represent the points
        return [[p[1], p[2]] for p in maxHeap]

        

        