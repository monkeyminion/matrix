import number
from number import Number

def is_frac(func):
    def check(self,*args):
        for arg in args:
            if not isinstance(arg,Fraction):
                raise NotFracException 
        def call():        
            return func(self,*args)
        return call()
    return check

class Fraction(Number):
    #TODO: Reduce fraction
    def __init__(self,numer,denom):
        self.numer = int(numer)
        self.denom = int(denom)
        super().__init__

    def __str__(self):
        return str(self.numer)+'/'+str(self.denom)

    def __repr__(self):
        return f'Fraction: self.numer {self.numer} self.denom {self.denom}'  

    
    def __add__(self,frac2):
        # self.is_frac(frac2)
        sum_denom = self.least_common_multiple(self.denom,frac2.denom)
        sum_numer = self.numer*(sum_denom //self.denom) + frac2.numer*(sum_denom // frac2.denom)
        return Fraction(sum_numer,sum_denom)
    
    
    def __sub__(self,frac2):
        subtracted_frac2 = Fraction(-1*frac2.numer,frac2.denom)
        return self.__add__(subtracted_frac2)

    
    def __mul__(self,frac2):
        numer = self.numer * frac2.numer
        denom = self.denom * frac2.denom
        return Fraction(numer,denom)

    
    def __truediv__(self,frac2):
        return self.__mul__(Fraction(frac2.denom,frac2.numer))

    
    def __eq__(self,frac2):
        return (self.numer == frac2.numer) and (self.denom == frac2.denom)
        
class NotFracException(Exception):
    pass

def test():
    test_q =  {((-3,7),(1,-10),"+"):(-37,70),
                ((-4,8),(-1,8),"+"):(-5,8),
                ((-2,6),(2,-5),"-"):(-11,15),
                ((-3,7),(-4,9),"-"):(1,63),
                ((-4,7),(-2,7),"-"):(-2,7),
                }
    for k,v in test_q.items():
        f1 = Fraction(k[0][0],k[0][1])
        f2 = Fraction(k[1][0],k[1][1])
        oper = {"+": f1 + f2,"-": f1 - f2,"*": f1 * f2, "/": f1 / f2}
        
        result = oper[k[2]]
        correct_ans = Fraction(v[0],v[1]) 
        if result == correct_ans:
            print(f"Error!,{k},{v}")
            print(str(f1),k[2],str(f2), " = ",str(result),"not",str(correct_ans))
        else:
            print(str(f1),k[2],str(f2), " = ",str(result))
test()
    