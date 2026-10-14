class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0

        start = 0
        end = len(heights) - 1

        while end > start:
            l, r = heights[start], heights[end]

            shorter = min(l, r)

            area = shorter * (end - start)

            if area > res:
                res = area

            if shorter == r:
                end -= 1
            else:
                start += 1
        return res