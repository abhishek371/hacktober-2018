memo = {}
memo[0]=1
memo[1]=1
import time 

def naive(x):
    if x < 0:
        return -1 
    elif x < 2 :
        return 1 
    return x*naive(x-1)

def dp(x):
    if x<0:
        return -1 
    if memo.get(x)==True:
        return memo[x]
    memo[x] = x * dp(x-1)
    return memo[x]

def main():
    N = 900
    print("--Calculating", N,"!--")
    start = time.time()
    x = naive(N)
    end = time.time()
    # print("Value : ",x)
    print("Time Taken : ",end-start)

    start = time.time()
    x =dp(N)
    end = time.time()
    # print("Value : ",x)
    print("Time Taken : ",end-start)





if __name__ == '__main__':
    main()