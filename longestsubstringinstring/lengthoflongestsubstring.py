def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        first_letter = s[-len(s)]
        substring = first_letter
        max = 0
        first = True
        for letter in s:
            if not first:
                if first_letter != letter:
                    substring += letter
                    if len(substring) > max:
                        max = len(substring)
                else:
                    first_letter = letter
                    substring = letter
            else:
                first = False
        return max

print(lengthOfLongestSubstring('asdasdasd'))