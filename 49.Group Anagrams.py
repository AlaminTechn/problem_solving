from typing import List

import collections

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = collections.defaultdict(list)
        
        print(dict)
        
        for str in strs:
              key = ' '.join(sorted(str))
              print("key",key)
              
              dict[key].append(str)
              
        return dict.values() # type: ignore
              
              
        
instance = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(instance.groupAnagrams(strs))    


        