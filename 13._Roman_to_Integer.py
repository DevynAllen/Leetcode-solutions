# 13. Roman to Integer
# Runtime: 48 ms, faster than 58.64%


class Solution:
    def romanToInt(self, s: str) -> int:
        values =  {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M':1000,
        }
        result = 0
        i = 0
        
        while (i < len(s)-1):
            currNumeral = s[i]
            nextNumeral = s[i+1]
            currValue = values[currNumeral]
            nextValue = values[nextNumeral]
            
            if (currValue >= nextValue):
                result+=currValue
                i+=1
            else:
                result+=(nextValue-currValue)
                i+=2

        if (i != len(s)):
            lastNumeral = s[i]
            lastValue = values[lastNumeral]
            result+=lastValue

        return result        
        
