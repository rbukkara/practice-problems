class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(filter(str.isalnum, s))
        s1 = s1.lower()
        if s1 == s1[::-1]:
            return True
        return False

    def test_palindrome(self, s: int, expected: bool):
        actual = self.isPalindrome(s)
        if actual == expected:
            print("pass")
        else:
            print("expected {0}, got {1}".format(expected, actual))


soln = Solution()
soln.test_palindrome("h*ell*o*w*orld", False)
soln.test_palindrome("aBba", True)
soln.test_palindrome("a Bb a  ", True)
soln.test_palindrome("aBbahy", False)
soln.test_palindrome("A man, a plan, a canal: Panama", True)
soln.test_palindrome("", True)



