from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
          
      if not matrix:
            return False
      
      m = len(matrix)
      n = len(matrix[0])
      print("m:",m, "n:",n)
      l = 0
      r = m * n
      print(l, r)
      
      while l < r:
            mid = (l + r) // 2
            print("mid:",mid)
            i = mid // n
            print("i:",i)
            j = mid % n
            print("j:",j)
            if matrix[i][j] == target:
                  return True
      
            if matrix[i][j] < target:
                  l = mid + 1
            else:
                  r = mid 
      return False
       
      



res = Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(res.searchMatrix(matrix, target))