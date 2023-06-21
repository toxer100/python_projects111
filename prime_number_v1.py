n= int(input('n = '))

list1= [2]

for i in range(3, n+1, 2):
    if (i > 10) and (i%10==5):
        continue
    for j in list1:
        if i%j == 0:
            break
    else:
        list1.append(i)
        
print(len(list1))