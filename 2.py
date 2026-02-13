# class parrot:
#     species = "bird"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# blu = parrot("BLu",10)
# woo = parrot("WOO",15)

# print("boo is also a {}".format(woo.__class__.species)) 

from typing import List

nums = [1,2,3,4,1]  # Renamed to avoid shadowing
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Test
sol = Solution()
print(sol.containsDuplicate(nums))  # Output: True