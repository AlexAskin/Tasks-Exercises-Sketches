# Search for a match in a string

my_str = 'abrakadabra'

num = 0

for i in my_str:
    if i == 'a':
        num += 1

print(f'{num} "a" in "{my_str}"')

print()

for i in range(len(my_str)):
    if i+1 > len(my_str)-1:
        break
    if my_str[i] == 'a' and my_str[i+1] == 'b':
        print('"ab" !')
        
print()
        
for i in my_str:
    if i in ('a', 'b'):
        print('a or b')
