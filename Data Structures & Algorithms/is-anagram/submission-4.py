class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sid = {}
        tid = {}

        for chars in s:
            if sid.get(chars): 
                sid[chars]+=1 
            else:
                sid[chars] = 1
            
        for chart in t: 
            if tid.get(chart):
                tid[chart]+=1 
            else:
                tid[chart] = 1

        return sid == tid

        