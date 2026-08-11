class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        rp = max(piles)
        lp = 1
        
        min_rate = max(piles)

        while lp <= rp: 

            rate = (rp + lp) // 2
            time = 0 
            for pile in piles: 
                time += (-(-pile // rate))


            if time > h: 
                lp = rate + 1
            else: 
                min_rate = rate
                rp = rate - 1
        
        return min_rate






        