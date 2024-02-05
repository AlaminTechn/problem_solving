class Solution:
    def climbStairs(self, n: int) -> int:
        one , two = 1, 1
        for i in range(n-1):
            print('i',i)
            temp = one 
            print(temp)
            one = one + two
            print('one',one)
            two = temp
            print('two',two)
        print('one :',one)
        return one
    
isnt = Solution()
val = 5
res = isnt.climbStairs(val)

print(res)