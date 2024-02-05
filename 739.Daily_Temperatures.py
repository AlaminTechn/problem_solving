from typing import List

# Time:O(n)
# Space: O(n)

class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0]* len(temperatures)
        print(result)
        stack = [] # a decreasing stack
        
        for i, temperature in enumerate(temperatures):
              
              while stack and temperature > temperatures[stack[-1]]:
                    print("temperatures[stack[-1]] :",temperatures[stack[-1]])
                    index = stack.pop()
                    print("index : ",index)
                    result[index] = i - index
                    print("result[index] : ",result[index])
                    
              stack.append(i)
              print(i, stack)
              
        return result

inst = Solution()

temperatures = [73,74,75,71,69,72,76,73]

res = inst.dailyTemperatures(temperatures)
print(res)