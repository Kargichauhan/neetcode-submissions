class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        # going through every value
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

        

         



# time space complexity == o(n) 
# o - size of the array
# o(n^2) - time
# space: o(n)
# sorting is the other method -- 
# hashset - 