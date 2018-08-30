# Karatsuba Multiplication for big numbers
# break down large number X*Y = (A*10^n+B)*(C*10^10+D)

def multiply_sm(x,y):
    lx = int(len(str(x)))
    ly = int(len(str(y)))
    lmax = max(lx,ly)

    if lmax < 4:
        return(x*y)
    elif lmax ==4 and (lx<4 or ly<4):
        return(x*y)
    elif lmax == 4:
        a = int(str(x)[:2])
        b = int(str(x)[2:4])
        c = int(str(y)[:2])
        d = int(str(y)[2:4])
        ac = a*c
        bd = b*d
        diff = (a+b)*(c+d)-bd-ac
        return(ac*(10000)+bd+diff*(100))
    else:
        # use recursion when number is more than 4 digits
        if lmax%4 !=0:
            lmax = (lmax//4+1)*4
        xdiff = lmax-lx
        ydiff = lmax-ly

        # append 0s to the front of the number
        if xdiff>0:
            for i in range(xdiff):
                x ="0"+str(x)
        if ydiff>0:
            for i in range(ydiff):
                y="0"+str(y)

        # split appended 'number' into abcd
        lmax_over2=int(lmax/2)
        a=int(str(x)[:lmax_over2])
        b=int(str(x)[lmax_over2:lmax])
        c=int(str(y)[:lmax_over2])
        d=int(str(y)[lmax_over2:lmax])

        # recursion calls
        ac = multiply_sm(a,c)
        bd = multiply_sm(b,d)
        diff = multiply_sm(a+b,c+d)-ac-bd
        return(ac*(10**lmax)+bd+diff*(10**lmax_over2))

# test case
x=3141592653589793238462643383279502884197169399375105820974944592
y=2718281828459045235360287471352662497757247093699959574966967627

print(multiply_sm(x,y))
