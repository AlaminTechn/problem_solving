class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        for r in range(numRows):
            increment = 2 * ( numRows - 1)
            print("increment : ",increment)
            for i in range(r, len(s), increment):
                res = res + s[i]
                print("res 1 : ",res)
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]
                    print("res 2 : ",res)

        return res
    


instance = Solution()
text = "APYYTHSTART"
res = instance.convert(text, 3)
print(res)