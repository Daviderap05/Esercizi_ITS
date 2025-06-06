# class Solution:

#     def intToRoman(self, num: int) -> str:
        
#         dictionary: dict= {
            
#             "M" : 1000,
#             "CM" : 900,
#             "D" : 500,
#             "CD" : 400,
#             "C" : 100,
#             "XC" : 90,
#             "L" : 50,
#             "XL" : 40,
#             "X" : 10,
#             "IX" : 9,
#             "V" : 5,
#             "IV" : 4,
#             "I" : 1

#         }

#         num_r: str = ""

#         if 1 <= num <= 3999:

#             for key, value in dictionary.items():
                
#                 while True:
                    
#                     if num - value >= 0:
                        
#                         num_r += key
#                         num -= value
                    
#                     else: 
                        
#                         break
                           
#             return num_r
                    
# n: Solution = Solution()

# n.intToRoman(3749)
# n.intToRoman(58) 
# n.intToRoman(1994)



# class Solution:

#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

#         if 0 < len(nums1) <= 1000 and 0 < len(nums2) <= 1000:
            
#             list3: list[int] = nums1 + nums2
#             list3.sort()
        
#             if len(list3) == 2:
                
#                 m: float = sum(list3) / 2   
            
#             elif len(list3) % 2 == 0:
                
#                 n: int = int(len(list3) / 2)
                
#                 m: float = (list3[n] + list3[n-1]) / 2
                
#             else:
                
#                 n: int = int(len(list3) / 2)
                
#                 m: float = list3[n]
                
#         elif not nums1:
            
#             if len(nums2) == 2:
                
#                 m: float = sum(nums2) / 2
            
#             elif len(nums2) % 2 == 0:
                
#                 n: int = int(len(nums2) / 2)
                
#                 m: float = (nums2[n] + nums2[n-1]) / 2
                
#             else:
                
#                 n: int = int(len(nums2) / 2)
                
#                 m: float = nums2[n]
                
#         elif not nums2:
            
#             if len(nums1) == 2:
                
#                 m: float = sum(nums1) / 2
            
#             elif len(nums1) % 2 == 0:
                
#                 n: int = int(len(nums1) / 2)
                
#                 m: float = (nums1[n] + nums1[n-1]) / 2
                
#             else:
                
#                 n: int = int(len(nums1) / 2)
                
#                 m: float = nums1[n]
                
#         else:
            
#             m: float = 0.0        
    
#         return m



# class Solution:
    
#     def reverse(self, x: int) -> int:
       
            
#             if x > 0:
                
#                 x = ''.join(reversed(str(x)))   
                
#                 return int(x)
            
#             else:
                
#                 x = ''.join(reversed(str(abs(x))))
                
#                 x_s: str = "-" + x
                
#                 if (-2)**31 <= int(x_s) <= (2**31) - 1:
                
#                     return int(x_s)
            
#                 else:
                    
#                     return 0
            

        
# n: Solution = Solution()
# n.reverse(0)



# class Solution:
    
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
        
#         if 2 <= len(nums) <= 10**4 and -10**9 <= target <= 10**9:
        
#             lista_t: list[int] = []
            
#             for j in range(0, len(nums) + 1):
            
#                 for i in range(j, len(nums) + 1):
                
#                     if i != len(nums):
                    
#                         if nums[i] + nums[i + 1] == target:
                            
#                             lista_t += [i, i+1]
#                     else:
                        
#                         break

#             return lista_t