# Longest Common Prefix

# Find the longest prefix shared across an array of strings.
# Teaches you to think about strings column-by-column rather than as a whole.


def longestCommonPrefix(strs: list[str]) -> str:

    # Protect against empty input
    if not strs:
        return ""

    # Start with an empty prefix and build it up character by character.
    prefix = ""
    # Iterate through the characters of the first string, and check if they match 
    # across all strings at the same position.
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs:
            # If we've reached the end of any string, or the character doesn't match, 
            # return the prefix we've built so far.
            if i >= len(s) or s[i] != char:
                return prefix
        prefix += char

    return prefix
