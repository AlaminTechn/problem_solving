'''
Time:O(logn)
Space: O(1)
'''


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
          
          
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
  


res = Solution()

nums = [-1,0,3,5,9,12]
target = 9

print(res.search(nums, target))