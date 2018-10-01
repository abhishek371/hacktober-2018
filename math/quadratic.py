
def quad(a,b,c):
    if a==0:
        if b==0:
            if c == 0 :
                return [True,True] 
            return [None,None]
        return [-c/b,None]
    
    D = b**2 - 4 * a * c 
    
    if D>=0:
        r1 = (-b + D**0.5 )/(2*a)
        r2 = (-b - D**0.5 )/(2*a)
        return [r1,r2] 
    
    # A +- iB 
    A = -b/(2*a)
    B = (-1*D)**0.5/(2*a)
    r1 = '' 
    r2 = ''
    r1 = str(A) + ' + ' + str(B) + 'i'
    r2 = str(A) + ' - ' + str(B) + 'i'
    return [r1,r2]
def main():
    print('--Ax^2 + Bx + C = 0 ')
    A = float(input('A:'))
    B = float(input('B:'))
    C = float(input('C:'))

    x = quad(A,B,C)

    print('Root 1 :' , x[0])
    print('Root 2 :', x[1])
    return 0

    pass 

if __name__ == '__main__':
    main()