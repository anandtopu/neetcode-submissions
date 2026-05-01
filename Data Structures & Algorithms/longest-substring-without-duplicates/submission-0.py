class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = Counter()
        left = right = 0
        longest = 0

        while right < len(s):
            r = s[right]
            char[r] += 1

            while char[r] > 1:
                l = s[left]
                char[l] -= 1
                left += 1
            longest = max(longest, right - left + 1)

            right +=1


            
        return longest
        