class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = ""
        smax = s1
        length = 0
        maxlength = 0
        for sa in s:
            print (sa)
            print (s1)
            print (s1.find(sa))
            if s1.find(sa) < 0:
                s1 += sa
                length += 1
            else:
                if length < maxlength:
                    length = 1
                    s1 = sa
                else:
                    maxlength = length
                    smax = s1
        return maxlength

if __name__ == '__main__':
    s = 'abca'
    print (Solution().lengthOfLongestSubstring(s))