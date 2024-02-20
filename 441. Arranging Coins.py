import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + math.sqrt(8 * n + 1)) // 2)
  

'''
Time : O(1)
Space : O(1)
'''