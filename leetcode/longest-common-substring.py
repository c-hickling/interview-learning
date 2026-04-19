# Longest Common Substring
# Find the longest substring shared across an array of strings.
# This is a more complex problem than longest common prefix.
def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    This function implements the sliding window technique to efficiently compute the length
    of the longest substring in the given string that contains no repeating characters.
    Args:
        s (str): The input string to analyze.
    Returns:
        int: The length of the longest substring without repeating characters.
    """
    seen = {}
    longest = 0
    left = 0

    for right, char in enumerate(s):
        # If the character has been seen and is within the current window, move 
        # the left pointer to the right of the last occurrence of the character.
        if char in seen and seen[char] >= left:
            # If we have found a repeated character, shift the window to the right 
            # to remove the first occurence (or left hand occurence) of the repeated character
            left = seen[char] + 1

        seen[char] = right
        longest = max(longest, right - left + 1)

    return longest
