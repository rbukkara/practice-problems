class Solution:

    def reverseWords(self, s: str) -> str:

        s = s.strip(" ")
        if s == "":
            return ""
        strings = s.split(" ")
        result = ""
        for string in strings:
            if string.strip() == "":
                continue
            result = string + " " + result

        result = result.strip()
        return result

    def testreverseWords(self, input_str: str, expected: str):

        actual = self.reverseWords(input_str)
        if actual == expected:
            print("pass")
        else:
            print("expected {0}, got {1}".format(expected, actual))


soln = Solution()
soln.testreverseWords("the sky is blue", "blue is sky the")
soln.testreverseWords("  hello world!  ", "world! hello")
soln.testreverseWords("a good   example", "example good a")
soln.testreverseWords("    ", "")


