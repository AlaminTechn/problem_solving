from typing import List


class Solution:
  def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        ans = 0
        
        prevEvenSum = 0
        prevOddSum = 0
        
        for i , a in enumerate(arr):
              currEvenSum = prevOddSum + ( (i + 1) // 2) * a
              currOddSum = prevEvenSum + ( i // 2+1) * a
              print(currEvenSum , currOddSum)
            #   print(currOddSum , )
              
              ans += currOddSum 
              prevEvenSum = currEvenSum
              prevOddSum = currOddSum
        return ans    
  
  
  
# Example usage:
arr = [1, 4, 2, 5, 3]
solution = Solution()
result = solution.sumOddLengthSubarrays(arr)
print(result)