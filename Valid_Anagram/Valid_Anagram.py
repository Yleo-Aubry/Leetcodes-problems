class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        occurence_s={}
        occurence_t={}

        for i in range(len(s)):
            occurence_s[s[i]] = occurence_s.get(s[i], 0) + 1
            occurence_t[t[i]] = occurence_t.get(t[i], 0) + 1

        return occurence_s==occurence_t


        
