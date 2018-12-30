import time,math
def timeit(func): ## times a function
    def callfunc(*args,**kwargs):
        initial_time = time.process_time()
        func(*args,**kwargs)
        end_time = time.process_time()
        return end_time - initial_time
    return callfunc
def test(timed_func):
    time = dict() # dict of n: time taken
    for n in range(500):
        time[n] = timed_func(n)
    for n,times in time.items():
        print(n,times)
    
####  ADD FRACTION  ###
# @timeit
# def get_factors(number=0) -> set:
#     try:
#         return {a for a in list(range(1,number+1)) for b in list(
#             range(1,number+1)) if a*b == number and a != 1}
#     except Exception as e:
#         print(f'Error : {e}')
#         return {}
# test(get_factors)
def get_factors(number=0) -> set:
    factors = list()
    for i in range(1,int(math.sqrt(abs(number)) + 1)):
        if number % i == 0:
            factors.append(i)
            factors.append(int(abs(number/i)))
    return set(factors)
def neg(num) -> str:
    '''Calculates sign +/- of num, then returns sign''' #---
    minus = num.count('-')
    if minus%2 == 1:
        sign = '-'   #odd number of -ves
    elif minus%2 == 0 or -1:
        sign = ''    #even/no -ves
    return sign

def greatest_common_factor(num1,num2):
    fac1 = get_factors(abs(num1))
    fac2 = get_factors(abs(num2))
    common = fac1.intersection(fac2)
    if len(common) == 0: # No common factors
        return None
    else:
        return max(common)

def least_common_multiple(num1,num2):
    gcf = greatest_common_factor(num1,num2)
    if gcf is None:
        return num1*num2
    else:
        return int((num1/gcf)*num2)

def addfrac(a,b,add=True):
    '''Adds/subtracts two fractions'''  #---
    
    alst, blst = a.split("/"), b.split("/")
    a_numer,a_denom = int(alst[0]), int(alst[1])
    b_numer, b_denom = int(blst[0]), int(blst[1])
    if add:
        sign = 1
    else:
        sign = -1

    denom = int(least_common_multiple(a_denom,b_denom))
    numer = int(a_numer*(denom/a_denom) + sign*b_numer*(denom/b_denom))
    return reduce(str(numer) +"/"+ str(denom))

###   DIVIDE FRACTION   ### ---
def divtwofrac(num,divnum):
    '''divide two fractions'''  #---
    # print('divtwofrac')
    nsign,  divsign = neg(num), neg(divnum)
    ndsign = nsign+divsign
    if ndsign == '' or ndsign == '--': # both nsign & divsign are -/+
        sign = ''
    else: #nsign & divsign have opposite signs
        sign = '-'
    num, divnum = num.replace('-',''), divnum.replace('-','')
    nslash, divslash = num.find('/'), divnum.find('/')
    nnumer, divnumer = int(num[:nslash:]), int(divnum[:divslash:])
    ndenom, divdenom = int(num[nslash+1::]), int(divnum[divslash+1::])
    assert divnumer,divdenom != 0
    return reduce(sign+str(nnumer*divdenom)+'/'+str(ndenom*divnumer))

def reduce(fracnum):
    '''Reduce a fraction'''  #---
    # print('reduce')
    sign = neg(fracnum)
    str_lst = fracnum.replace("-","").split("/")
    numer = int(str_lst[0])
    denom = int(str_lst[1])

    commonfac = greatest_common_factor(numer,denom)
    if(commonfac is None):
        return fracnum
    else:
        return sign + str(int(numer/commonfac))+"/"+str(int(denom/commonfac))

def multtwofrac(num,multnum):
    '''Multiply two fractions'''  #---
    nslash,mslash = num.find('/'), multnum.find('/')
    nnumer,ndenom = int(num[:nslash:]), int(num[nslash+1::])
    mnumer, mdenom = int(multnum[:mslash:]), int(multnum[mslash+1::])
    frac = str(nnumer*mnumer)+'/'+ str(ndenom*mdenom)
    return reduce(frac)

# print(addfrac('8/3','1/5',add=False))