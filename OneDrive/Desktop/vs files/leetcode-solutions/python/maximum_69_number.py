#leetcode 1323. python/maximum_69_number.py
class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        nums = n.replace("6","9",1)
        
        return int(nums)
                