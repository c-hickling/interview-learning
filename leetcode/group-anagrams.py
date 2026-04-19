# Group Anagrams
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        results_dict = defaultdict(list)

        for string in strs:
            # Sort the charactrers of each string and add them to a 
            # dictionary (anagrams of each other will be sorted under the same key)
            sorted_str = "".join(sorted(string))
            results_dict[sorted_str].append(string)

        return list(results_dict.values())