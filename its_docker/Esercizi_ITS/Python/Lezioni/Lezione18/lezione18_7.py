class Solution:

    def intToRoman(self, num: int) -> None:
        
        dictionary: dict= {
            
            "M" : 1000,
            "CM" : 900,
            "D" : 500,
            "CD" : 400,
            "C" : 100,
            "XC" : 90,
            "L" : 50,
            "XL" : 40,
            "X" : 10,
            "IX" : 9,
            "V" : 5,
            "IV" : 4,
            "I" : 1

        }

        num_r: str = ""

        if 1 <= num <= 3999:

            for key, value in dictionary.items():
                
                while True:
                    
                    if num - value >= 0:
                        
                        num_r += key
                        num -= value
                    
                    else: 
                        
                        break
                           
            print(num_r)
                    
n: Solution = Solution()

n.intToRoman(3749)
n.intToRoman(58) 
n.intToRoman(1994)