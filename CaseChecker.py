# Strings Case Checker:

# sring.islower()
# sring.isupper()
# sring.isalpha()

s = 'abc'

if s.islower():
    print(f'{s}:', s.islower())
else:
    print(f'{s}:', s.islower())


S = 'ABC'

if S.isupper():
    print(f'{S}:', S.isupper())
else:
    print(f'{S}:', S.isupper())


simple = 'Abc'

if simple.isalpha():
    print(f'{simple}:', simple.isalpha())
else:
    print(f'{simple}:', simple.isalpha())


# CodeWars kata: "Check same case":

def same_case(a, b):
    
    check_string = a + b
    
    s = check_string
    
    if not s.isalpha(): return -1
    
    result = 1 if s.islower() or s.isupper() else 0       

        
    return result


'''
Examples
'a' and 'g' returns 1
'A' and 'C' returns 1
'b' and 'G' returns 0
'B' and 'g' returns 0
'0' and '?' returns -1
'''

print(same_case('a', 'g'))
print(same_case('A', 'C'))
print(same_case('g', 'G'))
print(same_case('B', 'g'))
print(same_case('?', '-1'))
    
