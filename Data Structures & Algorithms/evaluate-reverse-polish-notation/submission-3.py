class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for elem in tokens: 

            # check to see if the elem is an integer in [-100, 100]
            if self.checkInteger(elem): 
                stack.append(int(elem))
            else: 
                process = ''

                var2 = stack.pop() 
                var1 = stack.pop()
                process += f'{var1} {elem} {var2}'
                
                stack.append(int(eval(process)))
        return stack[0]
                
    
    def checkInteger(self, s):
    # checking if it contains sign such as 
        if s[0] in ["+", "-"]:
            if s[1:].isdigit():
                return True
            return False
        
        if s.isdigit():
            return True
        return False


        