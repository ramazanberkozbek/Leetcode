"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
#1
from collections import defaultdict

def groupAnagram(strs):
    sozluk = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        sozluk[sorted_word].append(word)
    return list(sozluk.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(strs))


"""
#ilk aklıma gelen çözüm optimal değil    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sozluk = {}
        for i in strs:
            liste = []
            for j in i:
                liste += [ord(j)]
            liste = tuple(sorted(liste))
            if liste not in sozluk:
                sozluk[liste] = [i]
            else:
                sozluk[liste].append(i)
        finalListe = []
        for i in sozluk.values():
            finalListe.append(i)
        return finalListe 
    """