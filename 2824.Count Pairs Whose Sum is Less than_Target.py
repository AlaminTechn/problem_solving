from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        return sum(nums[i] + nums[j] < target
                  for i in range(len(nums))
                  for j in range(i+1,len(nums)))


# C++ implementation
''' 
int countPairs(vector<int>& nums, int target){
      int ans = 0;
      for( int i =0; i < nums.size(); ++i){
            for( int j = i+1; j < nums.size(); ++j){
                  if(nums[i] + nums[j] < target)
                  ++ans;
            }
      return ans;
      }
}






'''
   
   