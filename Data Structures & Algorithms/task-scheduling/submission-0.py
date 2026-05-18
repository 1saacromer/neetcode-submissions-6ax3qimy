class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks: 
            counts[ord(task) - ord('A')] += 1 
        
        counts.sort(reverse=True) 
        maxf = counts[0]
        idle = (maxf - 1) * n 

        for i in range(1, len(counts)): 
            idle -= min(counts[i], maxf - 1)

        return len(tasks) + max(0, idle)

        