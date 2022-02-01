import math
def list_squared(m, n):
    ints=[];i=m
    while i<=n:
        x=1;divisors2=[];xsum=0;
        while(x<=int(math.sqrt(i))):
            if(i%x==0):
                if(i/x==x):
                    divisors2.append(x)
                else:
                    divisors2.append(x)
                    divisors2.append(int(i/x))
            x+=1
        #divisors2.append(i)   
        for z in divisors2:
            xsum+=(z*z)
        if(math.sqrt(xsum)%1==0):
            ints.append([i,xsum])  
        i+=1
    return ints    