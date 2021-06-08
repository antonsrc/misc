# te_1

def gcd(a,b):
    a_ = a
    b_ = b
    
    if (b > a):
        a = a_
        b = b_
    
    t1 = a
    t2 = b
    step = 1
    while True:
        print('step = ' + str(step))
        t = t1%t2
        t1 = t2
        t2 = t
        print(t1)
        if t == 0:
            break
        step += 1

a = 462
b = 1071

gcd(a,b)