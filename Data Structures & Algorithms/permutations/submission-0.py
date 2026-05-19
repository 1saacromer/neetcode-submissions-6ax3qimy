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

        for i in range(len(nums)): 
            s = nums[i]
            l = nums[:i]
            r = nums[i+1:]
            lst = l + r 

            
            backtrack([s], lst)


        
        
        
        return res