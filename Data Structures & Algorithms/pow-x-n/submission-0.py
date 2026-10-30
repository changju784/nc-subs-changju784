class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Key points 
        1. Floating point precision
        2. x could be negative 
        3. power could be negative
        4. Use arithmetic Operations

        Brute Force 
        Negate n later return 1/result 
        Multiply x by n times for/while loop or recursion
        O(N) O(1)

        ex) 2 ** 6 
        (2 * 2 * 2) * (2 * 2 * 2)
        """
        is_neg = False 
        if n < 0: 
            n = -n
            is_neg = True 
        def get_pow(x, n): 
            if n == 0: 
                return 1 
            if x == 0: 
                return 0 
            result = get_pow(x * x, n//2)
            return x * result if n % 2 else result 
        result = get_pow(x, n)
        return 1/result if is_neg else result


        

