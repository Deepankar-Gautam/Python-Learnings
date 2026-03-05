l = [1,2,2,3,4,4,4,5,5,6]
dict = {}

for i in range (0, len(l)):
    if l[i] in dict:
        dict[l[i]]+= 1
    else:
        dict[l[i]] = 1

print (dict)

for i in dict:
    a = dict[i])

print (f"Repeating Characters Found : ")  