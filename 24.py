s=open('24_28765.txt').readline()
c=''
k=0
mx=0
for i in range(len(s)):
    c+=s[i]
    if c[-2:]=='BC':k+=1
    while k>180:
        if c[:2]=='BC':k-=1
        c=c[1:]
    mx=max(mx,len(c))
print(mx)