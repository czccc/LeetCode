#
# @lc app=leetcode.cn id=68 lang=python
#
# [68] 文本左右对齐
#

# @lc code=start
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans = []
        idx = 0
        while idx < len(words):
            cur_line = []
            cur_len = 0
            while idx < len(words) and cur_len + len(words[idx]) + len(cur_line) - 1 < maxWidth:
                cur_line.append(words[idx])
                cur_len += len(words[idx])
                idx += 1
            if len(cur_line) == 1 or idx == len(words):
                build = " ".join(cur_line)
                build += " " * (maxWidth - len(build))
                ans.append(build)
            else:
                spaces = maxWidth - cur_len
                each = spaces // (len(cur_line) - 1)
                res = spaces % (len(cur_line) - 1)
                build = ""
                for s in cur_line:
                    build += s
                    build += " " * min(spaces, each)
                    spaces -= min(spaces, each)
                    if res > 0:
                        build += " "
                        res -= 1
                        spaces -= 1
                ans.append(build)
        return ans
# @lc code=end


# TEST ONLY
import unittest

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().fullJustify

    def test_1(self):
        args = [["This", "is", "an", "example", "of", "text", "justification."], 16]
        ans = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [["What", "must", "be", "acknowledgment", "shall", "be"], 16]
        ans = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_3(self):
        args = [["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                 "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20]
        ans = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
