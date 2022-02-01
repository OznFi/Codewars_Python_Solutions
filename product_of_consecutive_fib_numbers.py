def productFib(prod):
    n=0;fn=0;fn1=0;found=False
    def fib(a):
        '''if(a==0):
            return 0
        if(a==1):
            return 1
        return fib(a-1)+fib(a-2)'''
        x, y = 0, 1
        for i in range(0, a):
            x, y = y, x + y
        return x
    while(True):
        if(fib(n)*fib(n+1)==prod):
            fn=fib(n);fn1=fib(n+1)
            found=True
            break
        if(fib(n)*fib(n+1)>prod):
            fn=fib(n);fn1=fib(n+1)
            break
        n+=1
    return[fn,fn1,found] 