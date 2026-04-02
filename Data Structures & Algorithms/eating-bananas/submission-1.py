class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Our search space spans from (1,...,max(piles))
        l, r = 1, max(piles)

        k_best = 0 

        while l <= r: 
            
            # k will be our midpoint in our search space of m 
            k = (l + r) // 2 

            # find the time to eat all piles of bananas given rate k 
            time = 0 
            for p in piles: 
                time += math.ceil(p / k)

            # keep track of the current best time 
            if time <= h:
                k_best = k 
                r = k - 1 
            else: 
                l = k + 1 
        

        return k_best 
        



