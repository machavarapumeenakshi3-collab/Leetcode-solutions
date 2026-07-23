class Solution(object):
    def lengthOfLongestSubstring(self, s):
        temp=set()
        left=0
        maxl=0
        for right in range(len(s)):
            while s[right] in temp:
                temp.remove(s[left])
                left+=1
            temp.add(s[right])
            maxl=max(maxl,right-left+1)
        return maxl




        