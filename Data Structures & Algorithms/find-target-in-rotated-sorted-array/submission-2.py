class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        min_idx = self.find_min(nums) 
        print(min_idx)
        if nums[min_idx] <= target <= nums[r]: 
            return self.binary_search(nums, target, min_idx, r)
        else: 
            return self.binary_search(nums, target, l, min_idx - 1)









    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int: 
        l, r = left, right 
        while l <= r: 
            m = (l + r) // 2 

            if nums[m] == target: 
                return m 
            if target > nums[m]: 
                l = m + 1 
            else: 
                r = m - 1  
        return -1




    def find_min(self, nums: List[int]) -> int: 
        l, r = 0, len(nums) - 1 

        while l < r: 
            m = (l + r) // 2

            if nums[m] < nums[r]: 
                r = m 
            else: 
                l = m + 1 

        return l