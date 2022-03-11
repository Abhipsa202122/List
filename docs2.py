'''2.Convert Character Matrix to single String;
    The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b','e','s','t']
    The String after join: gfgisbest'''
l= [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
a=['g','f','g']
b=['i','s']
c=['b','e','s','t']
l=a+b+c
d=l
i=0
while i<len(d):
    print(d[i],end="")
    i+=1