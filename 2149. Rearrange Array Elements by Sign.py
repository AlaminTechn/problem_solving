from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
          
        pos , neg = [] , []
        
        for n in nums:
              if n > 0:
                    pos.append(n)
              else:
                    neg.append(n)
        i = 0
        
        while 2 * i < len(nums):
              nums[2*i] = pos[i]
              nums[2 * i + 1] = neg[i]
              i += 1
        return nums


instance = Solution()

nums = [3,1,-2,-5,2,-4]

res = instance.rearrangeArray(nums)
print(res)

'''Time: O(n)
Space: O(n)'''


'''
Second Method:
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        pos = []
        neg = []

        for num in nums:
            (pos if num > 0 else neg).append(num)

        for p, n in zip(pos, neg):
            result += [p, n]
        return result


'''