import math 

def pi():       #using Gregory-Leibniz Series
    N = 10**5 
    sum = 0 
    for i in range(N):
        if i%2==0:
            sum = sum + 1/(2*i+1)
        else:
            sum = sum - 1/(2*i+1)
    return sum*4
def main():
    real_pi = math.pi
    our_pi = pi()
    print(real_pi,"\n",our_pi)
    print(real_pi==our_pi)
    return 0

if __name__ == '__main__':
    main()