from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for i in range(len(hours)):
              if hours[i] >= target:
                  res += 1
        return res
  
inst = Solution()

hours = [0,1,2,3,4]
target = 2

res = inst.numberOfEmployeesWhoMetTarget(hours, target)
print(res)