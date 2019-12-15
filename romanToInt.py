class Solution:

    num_value = dict()
    num_value["I"] = 1
    num_value["IV"] = 4
    num_value["V"] = 5
    num_value["IX"] = 9
    num_value["X"] = 10
    num_value["XL"] = 40
    num_value["L"] = 50
    num_value["XC"] = 90
    num_value["C"] = 100
    num_value["CD"] = 400
    num_value["D"] = 500
    num_value["CM"] = 900
    num_value["M"] = 1000

    def roman_to_int(self, s: str) -> int:
        ind = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return Solution.num_value[s]
        res = 0
        while ind < len(s):
            if s[ind: ind+2] in Solution.num_value:
                res += Solution.num_value[s[ind: ind+2]]
                ind += 1
            else:
                res += Solution.num_value[s[ind]]
            ind += 1

        return res

    def test_roman_to_int(self, s: str, expected: int):
        actual = self.roman_to_int(s)
        if actual == expected:
            print("pass")
        else:
            print("expected {0}, got {1}".format(expected, actual))


soln = Solution()
soln.test_roman_to_int("III", 3)
soln.test_roman_to_int("IV", 4)
soln.test_roman_to_int("IX", 9)
soln.test_roman_to_int("LVIII", 58)
soln.test_roman_to_int("MCMXCIV", 1994)
soln.test_roman_to_int("CIX", 109)
soln.test_roman_to_int("MLVIII", 1058)

