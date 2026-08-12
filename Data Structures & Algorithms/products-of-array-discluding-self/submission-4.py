class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        pre = [1] 
        for i in range(len(nums)): 
            pre.append(pre[i] * nums[i])
        pre.append(1)

        for i in range(len(nums)-1, -1, -1): 
            res[i] = pre[i] * pre[i+2]
            pre[i+1] = pre[i+2] * nums[i]
        

        return res 





        