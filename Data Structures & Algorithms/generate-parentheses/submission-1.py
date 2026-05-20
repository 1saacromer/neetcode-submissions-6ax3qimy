class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] 

        def backtrack(p, s): 

            if len(p) == 2 * n and s: 
                return 
            
            if len(p) == 2 * n:
                res.append(p)  
                return 

            p = p + '(' 
            s.append('(')
            backtrack(p, s[:]) 

            p = p[:-1]
            s.pop() 

            p = p + ')'
            if s and s[-1] == '(':
                s.pop() 
            else: 
                s.append(')')
            
            backtrack(p, s[:])



        backtrack("", []) 
        return res 