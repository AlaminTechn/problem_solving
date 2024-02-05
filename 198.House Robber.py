from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        
        for num in nums:
              db = max(prev1 , prev2 + num)
              print("db :",db)
              prev2 = prev1
              prev1 = db
              
        return prev1
  
        
instance = Solution()
nums = [1,2,3,1]
print(instance.rob(nums))