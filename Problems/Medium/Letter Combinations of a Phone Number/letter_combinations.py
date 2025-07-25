class Solution:
    def letterCombinations(self, digits: str) -> List[str]: 
        if not digits:
            return []       
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        def backtrack(idx,curr):
            if len(curr) == len(digits):
                result.append(curr[:])
                return
            digit = digits[idx]
            for char in digit_to_letters[digit]:
                backtrack(idx+1,curr+char)
        
        backtrack(0,"")
        return result
