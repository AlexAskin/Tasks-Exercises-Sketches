'''Some actions with "os" python module '''

import os

# CREATE DIR 
# путь относительно текущего скрипта
#os.mkdir("hello")

#print('Created dir "hello"')

# абсолютный путь
#!os.mkdir("c://somedir")
#!os.mkdir("C://Users//edi//Desktop//MY_PROJECTS//New_Project")

# REMOVING
# путь относительно текущего скрипта
#!os.rmdir("hello")
# абсолютный путь
#!os.rmdir("c://somedir/hello")

# RENAMING
# путь относительно текущего скрипта
#!os.rename('New Text Document.txt', 'Alex_Askinazi_notes.txt')
# абсолютный путь    
#!os.rename('C:\\Users\\edi\\Desktop\\MY_PROJECTS\\someText.txt', 'C:\\Users\\edi\\Desktop\\MY_PROJECTS\\MY_IMPORTANT_NOTES.txt')



print(os.name)
#print(os.environ)

#for i in os.environ:
    #print(i, ':' ,os.environ[i])
#     Current Way Directory!       |
print(os.getcwd())

print()
print()


#filename = input("Введите путь к файлу: ")

filename = input("Name -> ")

if os.path.exists(filename):
    print("Указанная Папка Существует:")
    print(os.getcwd() + f'\\{filename}')
else:
    print(f"Папка \"{filename}\" не существует")
    print(f"Сознана Папка: \"{filename}\"")
    os.mkdir(filename)

c = input()

#open('test.txt', 'w') # Crate txt-file





