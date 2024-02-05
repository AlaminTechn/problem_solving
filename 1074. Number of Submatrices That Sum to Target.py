import collections
from typing import List
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
          m = len(matrix)
          n = len(matrix[0])
          ans = 0
          
      #     Transforming Rows into Prefix Sums:
      
          for row in matrix:
                for i in range(1,n):
                      row[i] +=row[i-1]
                      
      # . Iterating Through Submatrices:
          for baseCol in range(n):
                for j in range(baseCol, n):
                      prefixCount = defaultdict(int)
                      prefixCount[0] = 1
                      summ = 0
                      for i in range(m):
                            if baseCol >0:
                                  summ -= matrix[i][baseCol-1]
                            summ +=matrix[i][j]
                            ans += prefixCount[summ - target]
                            prefixCount[summ] +=1
          return ans
                             
                 
inst = Solution()

matrix = [[904]]
target = 0
res = inst.numSubmatrixSumTarget(matrix,target)
print(res)