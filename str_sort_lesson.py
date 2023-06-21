list1 = ['ЯндеКс', "Мама", "авТо", '285пИво', 'ложка', '123','Три богатыря', 'Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО', 'поМидор', 'тЫк2ва', 'ваз2106']
list2 = []
a = 0

for s in list1:
    for i in s:
        if i.isupper() and a < 1:
            a += 1
            continue
        elif i.islower():
            continue
        else:
            a = 0
            break
    
    else:
        if a == 1:
            list2.append(s)
        a = 0

def list_append(m):
    n = [i for i in m if i.isupper() or i.isdigit() or i.isspace()]
    if len(n) == 1:
        return m
    else:
        return 0 
          
list3 = [list_append(m) for m in list1 if list_append(m) != 0]
list4 = list(filter(list_append, list1))
list5 = [list(filter(list_append, m)) for m in list1]
print(list2)
print(list3)
print(list4)
print(list5)