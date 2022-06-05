#
# @lc app=leetcode.cn id=29 lang=python
#
# [29] 两数相除
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == -2147483648:
                return 2147483647
            else:
                return -dividend
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        else:
            sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        ds_mul = []
        tmp = divisor
        while dividend - tmp >= tmp:
            ds_mul.append(tmp)
            tmp += tmp
        ds_mul.append(tmp)
        ans = 0
        for each in reversed(ds_mul):
            ans += ans
            if dividend >= each:
                ans += 1
                dividend -= each
        return ans if sign > 0 else -ans


# @lc code=end
# TEST ONLY
import unittest

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().divide

    def test_1(self):
        args = [10, 3]
        ans = 3
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [7, -3]
        ans = -2
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_3(self):
        args = [-2147483648, 2]
        ans = -1073741824
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
