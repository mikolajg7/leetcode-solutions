class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): # if the length of s and t isnt equal return False
            return False
        for i in set(s): # for every letter in set of s
            if s.count(i) != t.count(i): # if number of "i" letters in s isnt same as in t return False
                return False
        return True #otherwise return True

