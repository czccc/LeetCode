#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        s = 0
        e = m * n - 1
        while (s <= e):
            mid = (s + e) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                s = mid + 1
            else:
                e = mid - 1
        return False

# @lc code=end


# TEST ONLY
import unittest

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().searchMatrix

    def test_1(self):
        args1 = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        args2 = 3
        ans = True
        cur_ans = self._func(args1, args2)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args1 = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        args2 = 32
        ans = False
        cur_ans = self._func(args1, args2)
        self.assertEqual(cur_ans, ans)

    def test_3(self):
        args1 = [[1]]
        args2 = 1
        ans = True
        cur_ans = self._func(args1, args2)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
