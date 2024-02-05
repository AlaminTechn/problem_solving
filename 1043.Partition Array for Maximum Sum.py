from typing import List

class Solution:
      def maxSumAfterPartitioning(self, arr:List[int], k:int) -> int:
            
            # Method 01
            cache ={}
            
            def dfs(i):
                  if i in cache:
                        return cache[i]

                  
                  res = 0
                  current_max = 0
                  
                  for j in range(i, min(len(arr), i+k)):
                        current_max = max(current_max,arr[j])
                        window_size = j - i +1
                        res = max(res, dfs(j+1) + current_max * window_size)
                  cache[i] = res
                  return res
            
            return dfs(0)
      
            # # Method 02
            # n = len(arr)
            # dp = [0] * (n + 1)
            
            # for i in range(1, n+1):
            #       maxi = -math.inf
            #       for j in range(1,min(i,k) + 1):
            #             maxi = max(maxi, arr[i-j])
            #             dp[i] = max(dp[i], dp[i-j] + maxi * j)
            # return dp[n]
      
      