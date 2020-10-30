#
# @lc app=leetcode.cn id=393 lang=python
#
# [393] UTF-8 编码验证
#

# @lc code=start
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def get_one_number(n):
            for i in range(5):
                if n & (128 >> i) == 0:
                    return i
            return 5

        index = 0
        while index < len(data):
            L = get_one_number(data[index])
            if L == 1 or L == 5 or index + L - 1 >= len(data):
                return False
            elif L == 0:
                index += 1
            else:
                for i in range(L - 1):
                    if get_one_number(data[index + i + 1]) != 1:
                        return False
                index += L
        return True
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().validUtf8

    def test_1(self):
        args = [[197, 130, 1]]
        ans = True
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [[235, 140, 4]]
        ans = False
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
