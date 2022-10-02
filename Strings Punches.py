# Search for a match in a string
my_str = 'abrakadabra'
num = 0
for i in my_str:
    if i == 'a':
        num += 1

print(f'{num} "a" in "{my_str}"\n')


for i in range(len(my_str)):
    if i+1 > len(my_str)-1:
        break
    if my_str[i] == 'a' and my_str[i+1] == 'b':
        print('"ab" !') 
print()

for i in my_str:
    if i in ('a', 'b'): print('a or b')



# palindrome:
m = 'Rats live on no evil star!'

print(m[(len(m)-2): : -1] + m[-1])

print()


# _______________
# Reverse string:
string = "String"
reversed_string = string[::-1]
print(reversed_string) 


# ________________________________
# for Divide a string to the list:
string = "string"
print(list(string)) #['s', 't', 'r', 'i', 'n', 'g']

print()
# Camel Case String:
message = 'this is a testing message'
print(message.title())

print()
# Lower Case String:
message = 'THIS IS A TESTING MESSAGE'
print(message.lower())

print()
# Upper Case String:
message = 'this is a testing message'
print(message.upper())

print()
# Swap Case String:
message = 'This Is A Testing Message'
print(message.swapcase())

print()
# Cap Case String:
message = 'THIS IS A TESTING MESSAGE'
print(message.capitalize())


# Some Symbols...
print('conruentzia')

word = 'conruentzia\b'
print('conruentzia\b_')

print('\v','\f')

c = input()
print(c,'\a'*2)
 

print("oooo\raaa")


