from collections import OrderedDict

class Solution:

    roman_dict = OrderedDict()
    roman_dict[1000] = "M"
    roman_dict[900] = "CM"
    roman_dict[500] = "D"
    roman_dict[400] = "CD"
    roman_dict[100] = "C"
    roman_dict[90] = "XC"
    roman_dict[50] = "L"
    roman_dict[40] = "XL"
    roman_dict[10] = "X"
    roman_dict[9] = "IX"
    roman_dict[5] = "V"
    roman_dict[4] = "IV"
    roman_dict[1] = "I"

    def romanToInt(self, num: int) -> str:

        result = ""
        if num < 1 or num > 3999:
            print("invalid number")

        for key, value in Solution.roman_dict.items():
            while num >= key:
                result += value
                num = num - key
                if num == 0:
                    return result

        return result

    def test_roman_to_int(self, num: int, expected: str):

        actual = self.romanToInt(num)
        if actual == expected:
            print("pass")
        else:
            print("expected {0}, got {1}".format(expected, actual))


soln = Solution()
soln.test_roman_to_int(1, "I")
soln.test_roman_to_int(100, "C")
soln.test_roman_to_int(256, "CCLVI")
soln.test_roman_to_int(1994, "MCMXCIV")
soln.test_roman_to_int(1058, "MLVIII")
soln.test_roman_to_int(3999, "MMMCMXCIX")
