class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        res = [0] * len(temperatures) 

        for i, curr_temp in enumerate(temperatures): 
            while stack and curr_temp > stack[-1][1]:
                prev = stack.pop() 
                idx = prev[0]
                res[idx] = (i - idx)
            stack.append((i, curr_temp))


        return res





        