from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = dict()

        for x in strs:
            temp = ''.join(sorted(x))
            if temp in result_dict:
                result_dict[temp].append(x)
            else:
                result_dict[temp] = list()
                result_dict[temp].append(x)

        result = list()
        for x, y in result_dict.items():
            result.append(y)

        return result


    def test_group_anagrams(self, strs: List[str], expected: List[List[str]]):

        actual = self.groupAnagrams(strs)
        if actual == expected:
            print("pass")
        else:
            print("expected {0}, got {1}".format(expected, actual))


soln = Solution()
soln.test_group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"],
                        [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]])


