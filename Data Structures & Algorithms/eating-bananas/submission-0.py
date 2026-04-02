class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Our search space spans from (1,...,max(piles))
        m = max(piles) 

        l = 1 
        r = m 

        k_best = 0 

        while l <= r: 
            
            # k will be our midpoint in our search space of m 
            k = (l + r) // 2 

            # find the time to eat all piles of bananas given rate k 
            time = sum([((pile + k - 1) // k) for pile in piles])

            # keep track of the current best time 
            if time <= h:
                k_best = k 
                r = k - 1 
            else: 
                l = k + 1 
        

        return k_best 
        



