import time,math
def timeit(func): ## times a function
    def callfunc(*args,**kwargs):
        initial_time = time.process_time()
        func(*args,**kwargs)
        end_time = time.process_time()
        return end_time - initial_time
    return callfunc
def test(timed_func):
    def inside():
        time = dict() # dict of n: time taken
        for n in range(10000):
            time[n] = timed_func(n)
        for n,times in time.items():
            print(n,times)
    return inside

@timeit
def get_factors1(number=0) -> set:
    try:
        return {a for a in list(range(1,number+1)) for b in list(
            range(1,number+1)) if a*b == number and a != 1}
    except Exception as e:
        print(f'Error : {e}')
        return {}
@test
@timeit
def get_factors2(number=0) -> set:
    factors = list()
    for i in range(1,int(math.sqrt(abs(number)) + 1)):
        if number % i == 0:
            factors.append(i)
            factors.append(int(abs(number/i)))
    return set(factors)
get_factors2()
#print(get_factors2(-16))