def f(a,b,p):
    if a+b>=65 and p==3: return True
    if a+b>=65 and p==2: return False
    if a+b<65 and p==3: return False
    if p%2==0: return f(a+1,b,p+1) or f(a*3,b,p+1) or f(a,b+1,p+1) or f(a,b*3,p+1)
    if p % 2 == 1: return f(a + 1, b, p + 1) or f(a * 3, b, p + 1) or f(a, b + 1, p + 1) or f(a, b * 3, p + 1)
for s in range(1,59):
    if f(6,s,1):
        print(s)
        break