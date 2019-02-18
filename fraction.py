import number,exceptions
from number import Number
from exceptions import NotFracException

def is_frac(func):
    def assert_frac(self,*args):
        for arg in args:
            if not isinstance(arg,Fraction):
                raise exceptions.NotFracException 
        def call():        
            return func(self,*args)
        return call()
    return assert_frac

def reduce_dec(func):
    def reduce_output(self, *args):
        func_output = func(self, *args)
        if isinstance(func_output,Fraction):
            func_output.reduce()
        return func_output
    return reduce_output
        
class Fraction(Number):
    #TODO: Reduce fraction
    def __init__(self,numer,denom=1):    
        self.numer = int(numer)
        self.denom = int(denom)
        self.reduce()
        super().__init__

    @reduce_dec
    def __str__(self):
        if self.denom != 1: 
            return str(self.numer)+'/'+str(self.denom)
        else:
            return str(self.numer)

    @reduce_dec
    def __repr__(self):
        return f'Fraction: self.numer {self.numer} self.denom {self.denom}'  
    
    @reduce_dec
    @is_frac
    def __add__(self,frac2):
        sum_denom = self.least_common_multiple(self.denom,frac2.denom)
        sum_numer = self.numer*(sum_denom //self.denom) + frac2.numer*(sum_denom // frac2.denom)
        return Fraction(sum_numer,sum_denom)
    
    @reduce_dec
    @is_frac
    def __sub__(self,frac2):
        subtracted_frac2 = Fraction(-1*frac2.numer,frac2.denom)
        return self.__add__(subtracted_frac2)

    @reduce_dec
    @is_frac
    def __mul__(self,frac2):
        numer = self.numer * frac2.numer
        denom = self.denom * frac2.denom
        return Fraction(numer,denom)

    @reduce_dec
    @is_frac
    def __truediv__(self,frac2):
        return self.__mul__(Fraction(frac2.denom,frac2.numer))

    
    def __eq__(self,frac2):
        try:
            return (self.numer == frac2.numer) and (self.denom == frac2.denom)
        except AttributeError:
            if isinstance(frac2,int):
                return (self.numer == frac2) and (self.denom == 1)
        
    def reduce(self):
        if self.denom < 0:
            self.numer, self.denom = - self.numer, -self.denom
        if self.numer == 0 and self.denom != 1:
            self.denom = 1
            return
        gcf = self.greatest_common_factor(self.numer,self.denom)
        if gcf is not None:
            self.numer = int(self.numer / gcf)
            self.denom = int(self.denom / gcf)



def test(test_q):
    for k,v in test_q.items():
        f1 = Fraction(k[0][0],k[0][1])
        f2 = Fraction(k[1][0],k[1][1])
        oper = {"+": f1 + f2,"-": f1 - f2,"*": f1 * f2, "/": f1 / f2}
        
        result = oper[k[2]]
        correct_ans = Fraction(v[0],v[1]) 
        if result != correct_ans:
            print(f"Error!,{k},{v}")
            print(str(f1),k[2],str(f2), " = ",str(result),"not",str(correct_ans))
    print('done')

add_sub =  {((-3,7),(1,-10),"+"):(-37,70),
                ((-4,8),(-1,8),"+"):(-5,8),
                ((-2,6),(2,-5),"-"):(1,15),
                ((-3,7),(-4,9),"-"):(1,63),
                ((-4,7),(-2,7),"-"):(-2,7),
                }
mult = {((3,8),(1,10),'*'):(3,80),
            ((5,1),(19,4),'*'):(95,4),
            ((2,1),(29,8),'*'):(29,4),
            ((5,7),(4,6),'*'):(10,21),
            ((3,1),(26,4),'*'):(39,2),
            ((7,10),(5,1),'*'):(7,2),
            ((3,8),(4,1),'*'):(3,2),
            ((38,7),(27,8),'*'):(513,28)
            }
div = {((2,1),(11,2),'/'):(4,11),
            ((4,1),(8,5),'/'):(5,2),
            ((3,1),(2,8),'/'):(12,1),
            ((4,1),(11,4),'/'):(16,11),
            ((5,1),(6,4),'/'):(10,3),
            ((20,6),(12,5),'/'):(25,18),
            ((9,2),(10,8),'/'):(18,5),
            ((25,7),(9,3),'/'):(25,21)
            }

    