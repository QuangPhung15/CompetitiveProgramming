from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        words_line, words_length = [], 0

        for w in words:
            if (words_length + len(words_line) + len(w) > maxWidth):
                line = ""
                remain = maxWidth - words_length
                spaces_between = remain // max(1, len(words_line) - 1)
                spaces_extra = remain % max(1, len(words_line) - 1)

                for word in words_line:
                    line += word + " " * (spaces_between + min(1, spaces_extra))
                    spaces_extra = max(0, spaces_extra - 1)
                
                res.append(line[:maxWidth])
                words_line, words_length = [], 0
            
            words_line.append(w)
            words_length += len(w)

        last_line = " ".join(words_line)
        trailing_spaces = maxWidth - len(last_line)
        res.append(last_line + " " * trailing_spaces)
        
        return res

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where 
N = length of list words
"""