'''8.Write a Python program to find the list with maximum and minimum length.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])'''
l=[[5,4],[6,9,8,3],[2,7,8,9]]
i=0
m=l[0]
   # m1=l[0]
   # c=0
   # c1=0
while i<len(l):
    if l[i]<m:
       m=l[i]
           #c+=1
        #elif l[i]<m1:
           #m1=l[i]    
           #c1+=1
    i+=1
print(m)
