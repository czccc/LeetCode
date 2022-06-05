#
# @lc app=leetcode.cn id=57 lang=python
#
# [57] 插入区间
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        cur = 0
        while cur < len(intervals) and intervals[cur][1] < newInterval[0]:
            ans.append(intervals[cur])
            cur += 1
        ans.append(newInterval)
        while cur < len(intervals):
            if intervals[cur][0] <= ans[-1][1]:
                ans[-1][0] = min(ans[-1][0], intervals[cur][0])
                ans[-1][1] = max(ans[-1][1], intervals[cur][1])
            else:
                ans.append(intervals[cur])
            cur += 1
        return ans
# @lc code=end


# TEST ONLY
import unittest

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().insert

    def test_1(self):
        args = [[[1, 3], [6, 9]], [2, 5]]
        ans = [[1, 5], [6, 9]]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]]
        ans = [[1, 2], [3, 10], [12, 16]]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_3(self):
        args = [[], [4, 8]]
        ans = [[4, 8]]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_4(self):
        args = [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [24, 28]]
        ans = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16], [24, 28]]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_5(self):
        args = [[[3, 5], [6, 7], [8, 10], [12, 16]], [1, 2]]
        ans = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
