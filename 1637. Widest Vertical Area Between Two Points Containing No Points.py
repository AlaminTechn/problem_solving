from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        points.sort()
        res = 0
        for i in range(len(points)-1):
              res = max(res, points[i+1][0] - points[i][1])
        return res
  
  
inst = Solution()
points = [[8,7],[9,9],[7,4],[9,7]]
res = inst.maxWidthOfVerticalArea(points)
print(res)