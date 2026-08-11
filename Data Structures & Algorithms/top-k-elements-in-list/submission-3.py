class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # sinlge pass freq counter
        freq = {}
        for num in nums:
            if num in freq: 
                freq[num]+=1
            else: 
                freq[num] = 1

        # minheap sorting logic based of 0-index
        minheap = [] 
        for num in freq.keys():
            heapq.heappush(minheap, (freq[num], num))
            if len(minheap) > k: 
                heapq.heappop(minheap)
        
        # list comprehension, grabbing values left in minheap 
        return [pair[1] for pair in minheap]
        
        

        