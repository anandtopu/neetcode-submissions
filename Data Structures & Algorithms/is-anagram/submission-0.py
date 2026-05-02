class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Validate that all characters are lowercase English letters
        for char in s + t:
            if not ('a' <= char <= 'z'):
                # Fall back to hash map for non-lowercase characters
                return self.isAnagram_hash_map(s, t)

        # Create array for 26 lowercase letters
        char_count = [0] * 26

        # Increment for chars in s, decrement for chars in t
        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
            char_count[ord(t[i]) - ord('a')] -= 1

        # All counts should be zero if anagram
        return all(count == 0 for count in char_count)

    def isAnagram_hash_map(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        # Count characters in first string
        char_count: Dict[str, int] = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Verify counts match in second string
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False

        return True