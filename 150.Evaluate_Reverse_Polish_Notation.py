from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        op = {
              '+': lambda a, b : a + b,
              '-': lambda a, b : a - b,
              '*': lambda a, b : a * b,
              '/': lambda a, b : int(a / b),
        }
        
        for token in tokens:
              if token in op:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(op[token](a,b))
              else:
                    stack.append(int(token))
                    
        return stack.pop()
  
instance = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
res = instance.evalRPN(tokens)
print(res)
