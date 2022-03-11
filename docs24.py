'''24.Remove duplicates from a list.
List = [1,2,3,1,2,2]
Output: [1,2,3]'''
l=[1,2,3,1,2,2]
i=1
while i<len(l):
    if l[i] in l[:i]:
       l.pop(i)
    else:
        i+=1
print(l)        
#i=1
#while i<len(l):
#    if l[i]%2!=0:
#       print(l[i])
#    i+=1   


