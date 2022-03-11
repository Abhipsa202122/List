'''9.Write a Python program to scramble the letters of string in a given list. 
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
After scrambling the letters of the strings of the said list:
['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']'''
l = ['Python', 'list', 'exercises', 'practice', 'solution']
temp = []
for i in l:
    for j in i:
        temp.append(j)
        random.shuffle(temp)
        l = l[1::]
        l.append("".join(temp))
        temp = []
print(l)
