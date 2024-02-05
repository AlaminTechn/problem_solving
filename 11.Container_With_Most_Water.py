from typing import List
class Solution:
  def maxArea(self, height: List[int]) -> int:
    ans = 0 
    start = 0
    end = len(height) - 1

    while start < end :
      minHeight = min(height[start], height[end])
      print ('minHeight',minHeight)
      ans = max(ans, minHeight * ( end - start ))
      print ('ans',ans,'\n')
      if height[start] < height[end] :
        start += 1
      else :
        end -= 1

    return ans
  
isn = Solution()
arr = [1,8,6,2,5,4,8,3,7]
res = isn.maxArea(arr)
print (res)



