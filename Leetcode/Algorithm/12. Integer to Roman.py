class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        mapping = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }

        for k, v in mapping.items():
            count = num // v
            res += k * count
            num %= v
        
        return res
    
"""
Time Complexity: O(13) = O(1)
Space Complexity: O(1)
"""