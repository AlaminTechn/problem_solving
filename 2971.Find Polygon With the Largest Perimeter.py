from typing import List


class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
        prefix = sum(nums)
        
        for num in sorted(nums, reverse=True):
              prefix -= num
              
              if prefix > num:
                    return prefix + num
        return -1
  
res = Solution()

nums = [5,5,5]

print(res.largestPerimeter(nums))