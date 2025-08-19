class Solution:
    def singleNumber(self, nums: List[int]) -> int:
         dicct= {}
         for n in nums:
            if n in dicct:
                dicct[n]  += 1
            else:
                dicct[n] = 1  
         for key, value in dicct.items():
            if value == 1:
                return key     