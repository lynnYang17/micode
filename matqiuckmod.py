import sys
import numpy as np

def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            result = (result * b) % m
        e >>= 1
        b = (b*b) % m
    return result

while True:
    line = sys.stdin.readline()
    line = line.strip()
    a,b,c,d,mod,n = line.split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    mod = int(mod)
    n = int(n)
    if n == 1:
        ans = a % mod
        ans = str(ans)
        if len(ans) > 9:
            ans = ans[:9]
        else:
            p = ''
            for i in range(9-len(ans)):
                ans = '0'+ans
    else:
        mat = np.matrix([[1,1],[1,0]])
        xa = fastExpMod(mat, n-1, mod).getA()[0][0]
        xb = xa+n-2
        ansa = fastExpMod(a, xa, mod)
        ansb = fastExpMod(b, xb, mod)
        x = int(((((n-1)%mod) * ((n-2)%mod)) % mod) / 2)
        ansc = fastExpMod(c, x, mod)
        ans = (((ansa * ansb) % mod) * ansc) % mod
        ans = str(ans)
        if len(ans) > 9:
            ans = ans[:9]
        else:
            p = ''
            for i in range(9-len(ans)):
                ans = '0'+ans
    print(ans)
