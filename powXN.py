class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        if(n == 0):
            return 1
        elif(n < 0):
            return 1 / self.myPow(x, -n)
        elif(n % 2 != 0):
            return x * self.myPow(x, n-1)
        else:
            return self.myPow(x * x, n/2)
        
        
        #return pow(x,n)
