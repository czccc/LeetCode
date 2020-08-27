#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def quickMul(n):
            ans = 1.0
            x_contribute = x
            while n:
                if n % 2 == 1:
                    ans *= x_contribute
                x_contribute *= x_contribute
                n //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
# @lc code=end


# TEST ONLY
import unittest

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().myPow

    def test_1(self):
        args = [2.10000, 3]
        ans = 9.26100
        cur_ans = self._func(*args)
        self.assertAlmostEqual(cur_ans, ans)

    def test_2(self):
        args = [2.00000, 10]
        ans = 1024.00000
        cur_ans = self._func(*args)
        self.assertAlmostEqual(cur_ans, ans)

    def test_3(self):
        args = [2.00000, -2]
        ans = 0.25000
        cur_ans = self._func(*args)
        self.assertAlmostEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
