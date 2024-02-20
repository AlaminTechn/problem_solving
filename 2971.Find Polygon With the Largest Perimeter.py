from typing import List


class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
        prefix = sum(nums)
        print(prefix)
        
        for num in sorted(nums, reverse=True):
            #    Subtract the current element
              prefix -= num
            #   print(prefix)
              
              if prefix > num:
                    return prefix + num
        return -1
  
# res = Solution()

# nums = [5,5,5]

# print(res.largestPerimeter(nums))