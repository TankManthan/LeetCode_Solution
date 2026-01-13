class Solution:
    def isPalindrome(self, x: int) -> bool:
        t=x
        if x < 0:
            return False
        else:
            nX=str(x)
            nX=int(nX[::-1])
            if nX == t:
                return True
            return False
obj = Solution()
print(obj.isPalindrome(121))