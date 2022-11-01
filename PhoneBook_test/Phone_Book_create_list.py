''' Phone Book Creation'''

import random

names = [
"Amy",
"Evelyn",
"Bryan",
"Jessica",
"Andrea",
"Carolyn",
"Roger",
"John",
'Willson',
"Zaltan",
"Laura",
"Kevin",
"Joseph",
"Emma",
"Emma",
"Vincent",
"Vincent",
"Emma",
"Emma",
"Emma",
"Vincent",
"Hannah",
"Jeremy",
"Mark",
"Vincent",
"Ronald",
"Aaron",
"Joan",
"Joan",
"Joan",
]

th1_len = len(names)

print('First Lengrh of [names]', th1_len)
# Отсортировать [names] по алфавиту:

names.sort()

#for i in names: print(i)



check_names = []
add_fix = 0

matched_names = []#встречались ранее

for i in names:
    if i in check_names:
        print('!!!! MATCH !!!!:', i, ' += 1')

        #add_fix = 0
        
        if i not in matched_names:
            matched_names.append(i)
            add_fix = 0    
        
        add_fix += 1
        i = i + str(add_fix)
        
    check_names.append(i)
    
names = check_names #= []

num = 0
print('matched_names',matched_names)


for i in names:
    num += 1
    print(i)


print(num)


numbers = []



for i in range(len(names)):
    some_number = '+95'
    for i in range(8):
        if i == 0:
            r_num = random.randint(0,3)
        else:
            r_num = random.randint(0,9)
        some_number += str(r_num)
        
    numbers.append(some_number)
    #print(some_number)
    
for i in numbers:
    print(i)

    
print()
print()
# Добавляются элементы в словарь так:
#   dictionary_name[key] = value

data_base_numbers = {}










for i in range(len(names)):
    data_base_numbers[names[i]] = numbers[i]


d = data_base_numbers

num = 0

for i in d:
    num += 1
    print( i , ':' , d[i] )

print() 
#print(num)

if num == th1_len: print(f'\n{num} - OK!\n')



with open("data_base_numbers.txt", "w") as file:
    file.write("")
    #file.write("hello world")

with open("data_base_numbers.txt", "a") as file:
    for i in d:
        add_srting = i + ' : ' + d[i] + '\n'
        file.write(add_srting)
