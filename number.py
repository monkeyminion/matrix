import math
class Number:
    def __init__(self):
        pass
    
    def get_factors(self,number=0) -> set:
        factors = list()
        for i in range(1,int(math.sqrt(abs(number)) + 1)):
            if number % i == 0:
                factors.append(i)
                factors.append(int(abs(number/i)))
        return set(factors)

    def greatest_common_factor(self,num1,num2):
        fac1 = self.get_factors(abs(num1))
        fac2 = self.get_factors(abs(num2))
        common = fac1.intersection(fac2)
        if len(common) == 0: # No common factors
            return None
        else:
            return max(common)

    def least_common_multiple(self,num1,num2):
        gcf = self.greatest_common_factor(num1,num2)
        if gcf is None:
            return num1*num2
        else:
            return int((num1/gcf)*num2)
