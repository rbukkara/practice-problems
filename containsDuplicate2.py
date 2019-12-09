from typing import List, Dict


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(nums) == len(set(nums)):
            return False
        task_dic = {}
        for x in nums:
            if x in task_dic:
                task_dic[x] += 1
            else:
                task_dic[x] = 1

        for key in task_dic.keys():

            if task_dic[key] > 1:
                indices = [i for i, x in enumerate(nums) if x == key]
                for i in indices:
                    for j in indices:
                        if i != j and abs(i - j) <= k:
                            return True

        return False

    def test_containsNearbyDuplicate(self, tasks: List[str], n: int, expected_res: int):

        actual = self.containsNearbyDuplicate(tasks, n)
        if actual == expected_res:
            print("pass")
        else:
            print("expected {0}, got {1}".format(expected_res, actual))


task_sch = Solution()
task_sch.test_containsNearbyDuplicate([1, 0, 1, 1], 1, True)
task_sch.test_containsNearbyDuplicate([1, 2, 3, 1], 3, True)
task_sch.test_containsNearbyDuplicate([99, 99], 2, True)
task_sch.test_containsNearbyDuplicate([0,1,2,3,4,0,0,7,8,9,10,11,12,0], 1, True)
task_sch.test_containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2, False)



