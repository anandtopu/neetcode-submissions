class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            # Compute current area
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            # Move the pointer at the shorter bar inward
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res

        