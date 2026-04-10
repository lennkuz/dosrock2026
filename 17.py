a=open('17_28762.txt').readlines()
a=[int(x) for x in a]
mn=10**20
for x in a:
    if x%23==0:
        if x<mn:mn=min(x,mn)
print(mn)
k=0
r=[]
for i in range(len(a)-1):
    if len([int(x) for x in a[i:i+2] if x%mn==0])>=1:
        k+=1
        r.append(sum(a[i:i+2]))
print(k,max(r))