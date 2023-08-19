# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lengthofStrings = []
        stringtoreturn = ""
        for i in strs:
            lengthofStrings.append(len(i))
        lengthofStrings.sort()
        lengthofsmallestststring = lengthofStrings[0]
        for j in range(0, lengthofsmallestststring):
            for i in range(0, len(strs) - 1):
                if strs[i][j] == strs[i + 1][j]:
                    continue
                else:
                    return stringtoreturn
            stringtoreturn = stringtoreturn + strs[0][j]
        return stringtoreturn


A = Solution()
result = A.longestCommonPrefix(["flower","flow","flight"])
print(result)
