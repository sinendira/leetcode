import re

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        min_length = 6
        max_length = 20
        max_repeat = 2
        
        def count_replacements(pw):
            replacements = 0
            one_seq, two_seq = 0, 0
            i = 2
            while i < len(pw):
                if pw[i] == pw[i - 1] == pw[i - 2]:
                    length = 2
                    while i < len(pw) and pw[i] == pw[i - 1]:
                        length += 1
                        i += 1
                    replacements += length // 3
                    if length % 3 == 0:
                        one_seq += 1
                    elif length % 3 == 1:
                        two_seq += 1
                else:
                    i += 1
            return replacements, one_seq, two_seq

        n = len(password)
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'\d', password))
        
        missing_types = int(not has_lower) + int(not has_upper) + int(not has_digit)
        
        replacements, one_seq, two_seq = count_replacements(password)
        
        if n < min_length:
            return max(missing_types, min_length - n)
        
        elif n <= max_length:
            return max(missing_types, replacements)
        
        else:
            deletions = n - max_length
            replacements -= min(deletions, one_seq)
            replacements -= min(max(deletions - one_seq, 0), two_seq * 2) // 2
            replacements -= max(deletions - one_seq - 2 * two_seq, 0) // 3
            return deletions + max(missing_types, replacements)


