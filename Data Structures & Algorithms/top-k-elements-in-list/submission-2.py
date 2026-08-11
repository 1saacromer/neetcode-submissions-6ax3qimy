class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # sinlge pass freq counter
        freq = {}
        for num in nums:
            if num in freq: 
                freq[num]+=1
            else: 
                freq[num] = 1

        # create min-heap tuples 
        freq_nums = [(value, key) for key, value in freq.items()]


        # minheap sorting logic based of 0-index
        minheap = [] 
        for pair in freq_nums:
            heapq.heappush(minheap, pair)
            if len(minheap) > k: 
                heapq.heappop(minheap)
        
        # list comprehension, grabbing values left in minheap 
        return [pair[1] for pair in minheap]
        
        

        