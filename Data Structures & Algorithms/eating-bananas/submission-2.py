class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k_best = 0 

        while l <= r: 
            
            k = (l + r) // 2 

            time = 0 
            for p in piles: 
                time += math.ceil(p / k)

            if time <= h:
                k_best = k 
                r = k - 1 
            else: 
                l = k + 1 
        

        return k_best 
        



