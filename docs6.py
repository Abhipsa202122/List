'''6.Find the First Maximum, Second maximum, Third maximum number from the List.'''
n=[20,50,10,70,90]
m1=0
m2=0
m3=0
i=0
while i<len(n):
    if n[i]>m1:
       m3=m2
       m2=m1
       m1=n[i]
    elif n[i]>m2:
       m3=m2
       m2=n[i]
    elif n[i]>m3:
       m3=n[i]    
    i+=1
print(m1)
print(m2)
print(m3)
        

