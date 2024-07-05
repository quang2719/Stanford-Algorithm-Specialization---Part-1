class Solution:
    def karatsuba(self, num1, num2):
        """
        Multiplies two non-negative integers represented as 
        strings using the Karatsuba algorithm.

        Args:
            num1: First integer string.
            num2: Second integer string.

        Returns:
            The product of num1 and num2 as a string.
        """

        # Base case: single-digit numbers or empty string
        if num1 == "" or num2 == "":
            return "0"
        if len(num1) == 1 or len(num2) == 1:
            return str(int(num1) * int(num2))

        # Make num1 and num2 have the same length 
        # (add leading zeros if needed)
        n = max(len(num1), len(num2))
        num1 = num1.zfill(n) #123 -> 1,23->zfill-> 01,23
        num2 = num2.zfill(n)

        # Split numbers into halves
        half = n // 2
        a = num1[:half]
        b = num1[half:]
        c = num2[:half]
        d = num2[half:]

        # Recursive multiplications
        
        # Use self.karatsuba for recursive calls
        ac = self.karatsuba(a, c)  
        bd = self.karatsuba(b, d)
        ad_plus_bc = self.karatsuba(
                    str(int(a) + int(b)), str(int(c) + int(d))
            )
        ad_plus_bc = str(int(ad_plus_bc) - int(ac) - int(bd))

        # Combine results (with appropriate zero padding)
        return str(
            int(ac) * 10**(2 * (n - half)) + 
            int(ad_plus_bc) * 10**(n - half) + 
            int(bd)
        )
    def multiply(self, num1: str, num2: str) -> str:
        return self.karatsuba(num1, num2) # Directly return the result from karatsuba
a = Solution()
num1 = "3141592653589793238462643383279502884197169399375105820974944592"
num2 = "2718281828459045235360287471352662497757247093699959574966967627"
print(a.karatsuba(num1,num2))
