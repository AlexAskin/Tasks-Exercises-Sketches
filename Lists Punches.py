# ____________________________________
# Conditional Statements if/elif/else:
a = 5
b = 3

if a < b:
    res = a + b
else:
    res = a - b
print('result 1:',res)


# One-string method:
res = a + b if a < b else a - b

print('result  2:',res)



# ___________________
# List Comprehension:
my_list = [2,3,4,7,13]

dobled = []

for num in my_list:
    if num % 2 == 0:
        dobled.append(num*2)
    
print('dobled1:',dobled)

# One-string method:
dobled2 = [num*2 for num in my_list if num % 2 == 0]

print('dobled2:',dobled2)



# List.reverse():
arr = [0,1,2,3,4,5,6,7,8,9]
print('arr =', arr)

sum_arr = 0
for i in arr:
    #print(i)
    sum_arr += i

print('sum arr:', sum_arr)
arr.reverse()
print('arr.reverse() =', arr)




# __________________
# for Random Number:
import random
a = 1
b = 100
random_num = random.randint(a,b)  # a <= x <= b
print(random_num)





