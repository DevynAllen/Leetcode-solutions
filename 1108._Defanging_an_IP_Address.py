# 1108. Defanging an IP Address
# Runtime: 28 ms, faster than 71.44%

class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        
        for character in address:
            if character == '.':
                result+='[.]'
            else:
                result+=character
        
        return result
