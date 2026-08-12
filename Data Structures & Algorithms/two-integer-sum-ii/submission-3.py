class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1 
        
        while (numbers[l] + numbers[r]) != target: 
            total = numbers[l] + numbers[r]
            if total < target: 
                l += 1
            else: 
                r -= 1
    
        return [l+1, r+1]
        
        