from typing import List
import collections


class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    count = collections.Counter(arr)
    occurrences = set()

    for value in count.values():
      if value in occurrences:
        return False
      occurrences.add(value)
      print('occurrences',occurrences)
      print('value',value)
    return True
  

instance = Solution()
array = [1,2,2,1,1,3]
res = instance.uniqueOccurrences(array)
print(res)