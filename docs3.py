'''4.List product excluding duplicates.
    List = [6,1,3,5,6,3,1]
    Output: 60'''
list=[6,1,3,5,6,3,1]
i=0
a=0
s=0
while i<len(list):
    if list[i] not in a:
       a.append(list[i])
       s=s+(a[i]+a[i])
    i+=1
print(a)                
