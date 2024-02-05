
from typing import List

class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    i = 0

    for num in nums:
      if num !=val:
        nums[i] = num
        i+=1
      print(num , val)
    return i
  

isnt = Solution()
d = [1,2,2,3,4,5]
val = 2

res = isnt.removeElement(d,val)

print(res)