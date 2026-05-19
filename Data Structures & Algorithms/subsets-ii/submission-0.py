class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[] 
        nums.sort()



        def backtrack(i, p): 
            if i == len(nums): 
                res.append(p[:]) 
                return 

            p.append(nums[i])
            backtrack(i + 1, p) 

            p.pop() 

            while i < len(nums) - 1 and nums[i] == nums[i+1]: 
                i += 1 
            
            backtrack(i + 1, p)
        


        backtrack(0, [])
        return res 
        