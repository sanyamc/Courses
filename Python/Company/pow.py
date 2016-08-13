""" 
      Implement pow(x, n)

      From somewhere: METHOD 1
      We have just seen how to compute products in modular arithmetic (mod n) without ever looking at numbers larger than the square of n.
For powers ax (mod n) there is an even neater trick, which saves a lot of work, especially when x is large (and we'll need that in the RSA encryption algorithm later).

This trick is based on the method of calculating powers independently of modular arithmetic. Suppose we would like to calculate 1143. The straightforward method would be to multiply 11 by 11, then to multiply the result by 11, and so forth. This would require 42 multiplications. We can save a lot of multiplications if we do the following:

First write 43 as a sum of powers of 2: 
43 = 32 + 8 + 2 + 1

That means that 
Now 1143 = 1132 * 118 * 112 * 11 .

The calculation of the sequence 11, 112, 114, 118, 1116, 1132 requires 5 multiplications as each following term is the square of the previous. Now the calculation of the 43rd power requires three more multiplications. So, the trick allowed us to reduce the number of multiplications from 42 to 8.

METHOD 2:
https://en.wikipedia.org/wiki/Exponentiation_by_squaring



"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if(x==0):
            return 0
        if(n==0):
            return 1
        if(n<0):
            n=-n
            x=1/x
            
        y=1
        while(n>1):            
            if(n%2 == 0):
                x=x*x
                n=n/2
            else:
                y=x*y
                x=x*x
                n=(n-1)/2            
        return x*y


s=Solution()
print(s.myPow(2,4))
print(s.myPow(3,3))
print(s.myPow(2,5))



        