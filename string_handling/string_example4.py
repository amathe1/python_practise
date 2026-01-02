from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        # Compare the prefix with each string in the list
        for s in strs[1:]:
            while not s.startswith(prefix):
                # Shrink the prefix until it matches
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
