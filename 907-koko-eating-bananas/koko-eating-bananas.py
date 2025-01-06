class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        result = r

        while l <= r:
            k = (l+r)//2
            hours = 0
            for bananas in piles:
                hours += ceil(bananas/k)
            if hours <=h:
                result = min(k, result)
                r = k-1
            else:
                l = k+1
        return result