# Is Anagram

from collections import defaultdict

def isAnagram(self, s: str, t: str) -> bool:

# An anagram is a word or phrase formed by rearranging the letters of a different 
# word or phrase, typically using all the original letters exactly once.    
    if len(s) != len(t):
        return False

    letter_counts = defaultdict(int)

    for letter in s:
        letter_counts[letter] += 1

    for letter in t:
        letter_counts[letter] -= 1
        if letter_counts[letter] < 0:
            return False

    return True
