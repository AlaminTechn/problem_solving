import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
          count = collections.Counter(s)
          
          print("count",count)
          
          for i , c in enumerate(s):
                if count[c] == 1:
                      print("count i :",i)
                      return i
                      
          return -1


inst = Solution()

# s = "leetcode"
s = "loveleetcode"


res = inst.firstUniqChar(s)
print(res)  