'''Phone Book Searching'''

book = {}

names = []
numbers = []

with open("data_base_numbers.txt", "r") as file:
    for line in file:
        
        name = ''
        for i in line:
            if i == ' ': break
            name += i

        separete = False
        number = '+'  
        for i in line:
            
            if i == ' ': separete = True

            if separete is True:
                
                if i in ('0','1','2','3','4','5','6','7','8','9'):
                    number += i
                
        #dictionary_name[key] = value        
        book[name] = number 
            
        print(line, end="")

print()

#for i in book: print(i, book[i])

#print(len(book))

def Searching():
    what_name = input('\nSearch? -> ')
        

    found_res = []
    try:
        found = False

        for i in book:
            if what_name in i:
                res = i + ': ' +book[i]
                print(res, "   in!")
                found_res.append(res)
                found = True


        if len(what_name) == 1:
            AZ = what_name.upper()
            for i in book:
                if AZ == i[0]:
                    res = i + ': ' +book[i]

                    if res not in found_res:
                        found_res.append(res)
                        print(res)
                        found = True

                    
        Abc = what_name.title()
        
        for i in book:                
            if Abc in i:
                res = i + ': ' +book[i]
                if res not in found_res:
                    found_res.append(res)
                    print(res, " Abc in!")
                    found = True

        for i in book:
            if what_name in book[i]: 
                res = i + ': ' +book[i]
                if res not in found_res:
                    found_res.append(res)
                    print(res, " Abc in!")
                    found = True        


        if found is False:
            print('Not Found!')
        else:
            print()
            print('Result:')
            for i in found_res:
                print(i) 
        
    except:
        print('except: Not Found')


while True: Searching()
