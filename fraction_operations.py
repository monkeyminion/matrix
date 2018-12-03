####  ADD FRACTION  ###
def get_factors(number=0):
    try:
        return {a for a in list(range(2,number)) for b in list(
            range(2,number)) if a*b == number}
    except Exception as e:
        print(f'Error : {e}')

def get_common_factor(num1,num2):
    fac1 = get_factors(num1)
    fac2 = get_factors(num2)
    if num1 == num2 :#or len(fac1) == 0 or len(fac2) == 0:
        return None    
    elif num1 in fac2:
        #if num1 is a factor of num2
        return [num2, int(num2/num1)]
    elif num2 in fac1:
        #if num2 is a factor of num1
        return [num1,int(num1/num2)]

def addfrac(a,b,add=True):
    '''Adds/subtracts two fractions'''  #---
    aslash = a.index('/')
    bslash = b.index('/')
    a0, a2 = int(a[:aslash]),int(a[aslash+1::])
    b0, b2 = int(b[:bslash]),int(b[bslash+1::])
    f = get_common_factor(a2,b2)
    if add:
        one = 1
    else:
        one = -1
    if f: #if NOT None: (a2,b2 are factors)
        if a2 == f[0]:
            return str(a0 + one*b0*f[1]) +'/'+ str(a2)
        elif b2 == f[0]:
            return str(one*b0 + a0*f[1]) + '/'+str(b2)
    elif a2 == b2: # the denom of a,b are the same
        return str(a0+one*b0)+'/'+str(b2)
    else: # the demom of a,b are Not factors and are Not the same
        return str(a0*b2 + one*b0*a2) + '/' + str(a2*b2)

###   DIVIDE FRACTION   ### ---
def divtwofrac(num,divnum):
    '''divide two fractions'''  #---
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
    sign = neg(fracnum)
    fracnum = fracnum.replace('-','')
    slash = fracnum.find('/')
    numer = int(fracnum[:slash:])
    denom = int(fracnum[slash+1::])

    numfac = get_factors(numer)
    denomfac = get_factors(denom)

    if denom in numfac:#denom is a factor of numer
        divided = str(numer/denom)
        newnumer, newdenom = int(divided[:divided.find('.'):]),1
        return sign + str(newnumer)+'/'+str(newdenom)

    elif sorted(list(set(numfac).intersection(set(denomfac)))[1::],reverse=1):  #numer & denom share factor
        common = sorted(list(set(numfac).intersection(set(denomfac)))[1::],reverse=1)
        numdivided = numer/common[0]
        denomdivided = denom/common[0]
        newnumer, newdenom = int(numdivided), int(denomdivided)
        return reduce(sign+str(newnumer)+'/'+str(newdenom))

    else:  #unable to reduce
        return sign+fracnum
def multtwofrac(num,multnum):
    '''Multiply two fractions'''  #---
    nslash,mslash = num.find('/'), multnum.find('/')
    nnumer,ndenom = int(num[:nslash:]), int(num[nslash+1::])
    mnumer, mdenom = int(multnum[:mslash:]), int(multnum[mslash+1::])
    frac = str(nnumer*mnumer)+'/'+ str(ndenom*mdenom)
    return reduce(frac)

def neg(num):
    '''Calculates sign +/- of num, then returns sign''' #---
    minus = num.count('-')
    if minus%2 == 1:
        sign = '-'   #odd number of -ves
    elif minus%2 == 0 or -1:
        sign = ''    #even/no -ves
    return sign

