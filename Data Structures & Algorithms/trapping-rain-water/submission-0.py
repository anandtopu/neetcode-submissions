class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        for i in range(n):
            maxL = max(height[:i + 1]) if i > 0 else height[i]
            maxR = max(height[i:]) if i < n - 1 else height[i]
            total += max(0, min(maxL, maxR) - height[i])
        return total