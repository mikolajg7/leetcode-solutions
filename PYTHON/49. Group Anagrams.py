class Solution(object):
    def groupAnagrams(self, strs):
        anagram={}
        for s in strs:
            sort_s="".join(sorted(s)) #sort the word so it will be easier to find in dictionary
            if sort_s in anagram: # if in dictionary, add to the same index
                anagram[sort_s].append(s)
            else:
                anagram[sort_s]=[s] # in not to the dictionary add new list to dicionary
        return list(anagram.values())
