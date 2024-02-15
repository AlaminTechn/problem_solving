from typing import List
import math

class Solution:
  def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        result = -math.inf
        print(result)
        
        prefix =0
        numToMinPrefix = {}
        
        for num in nums:
              if num not in numToMinPrefix or numToMinPrefix[num] > prefix:
                    numToMinPrefix[num] = prefix
              prefix += num
              
              if num + k in numToMinPrefix:
                    result = max(result, prefix - numToMinPrefix[num + k])
              if num - k in numToMinPrefix:
                    result = max(result , prefix - numToMinPrefix[num - k])
                    
        return 0 if result == -math.inf else result
  

instance = Solution()

nums = [-1,-2,-3,-4]
k = 2
res = instance.maximumSubarraySum(nums, k)
print(res)

'''Time: O(n)
Space: O(n)'''