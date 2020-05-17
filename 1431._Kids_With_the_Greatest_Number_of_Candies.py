# 1431. Kids With the Greatest Number of Candies
# Runtime: 36 ms, faster than 76.07%

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNumber = max(candies)
        result = []
        
        for num in candies:
            total = num + extraCandies
            if (total >= maxNumber):
                result.append(True)
            else:
                result.append(False)

        return result
