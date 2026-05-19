class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        def backtrack(p, lst): 
            if len(p) == len(nums): 
                res.append(p[:])
                return 
            
            for n in lst: 
                if n not in p:
                    p.append(n) 
                    backtrack(p, lst)
                    p.pop()

            
        backtrack([], nums)

        return res