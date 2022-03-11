#magicsquare:
m=[[8,3,4],[1,5,9],[6,7,9]]
i=0
while i<len(m):
    j=0
    r=0
    c=0
    d=0
    r1=0
    r2=0
    r3=0
    c1=0
    c2=0
    c3=0
    d1=0
    d2=0
    s=0
    while j<len(m[i]):
        r=r1=r1+m[j][i]
        r2=r2+m[j][i]
        r3=r3+m[j][i]
        c=c1=c1+m[j][i]
        c2=c2+m[j][i]
        c3=c3+m[j][i]
        d=d1=d1+m[j][i]
        s=s+r+c+d
        j+=1
    i+=1
if r1==r2==r3==c1==c2==c3==d1==d2:
   print("magic square",r,c,d)
else:
   print("not")            
     