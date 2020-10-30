#
# @lc app=leetcode.cn id=401 lang=python
#
# [401] 二进制手表
#

# @lc code=start
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def read_time(watch):
            hour = watch >> 6 % 16
            minute = watch % 64
            if hour > 11 or minute > 59:
                return False, None
            else:
                return True, "{}:{:0>2}".format(hour, minute)

        def backtrack(i, n, watch):
            if n == 0:
                valid, time = read_time(watch)
                if valid:
                    ans.append(time)
                return
            for j in range(i, -1, -1):
                watch |= (1 << j)
                backtrack(j - 1, n - 1, watch)
                watch ^= (1 << j)

        ans = []
        watch = 0
        backtrack(9, num, watch)
        return ans
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().readBinaryWatch

    def test_1(self):
        args = [1]
        ans = ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
        cur_ans = self._func(*args)
        self.assertCountEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
