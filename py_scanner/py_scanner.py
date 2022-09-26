"script for scanning my Projects directories" #26/09/2022


import os
import natsort



print(os.getcwd())

cwd_str = os.getcwd() #C:\Users\edi\Desktop\MY_PROJECTS\py_scanner

#print(type(way_str))

project_dir_str = cwd_str[:32]
print(project_dir_str)



dir_list = natsort.natsorted(os.listdir(project_dir_str))
#print('\n'.join())  # Showing dir content

text_writing = ''

print()
for i in range(len(dir_list)):
    #print(f'{i+1}.',dir_list[i])

    
    get_info_file_path = project_dir_str + '\\' + dir_list[i] + '\\info.txt'

    print()
    print('_________________________________________')


    print(f'{i+1}.',get_info_file_path)
    bord_line = '_'*40
    text_writing += f'\n{bord_line}\n'
    
    text_writing += (f'{i+1}. {get_info_file_path}\n')
    

    print()
    with open(get_info_file_path, "r") as file: # for READING

        for line in file:
            print(line, end="")
            text_writing += line+'\n'
        print()
                
    print('_________________________________________')

    text_writing += f'\n{bord_line}\n\n'
    
with open("result_scanning.txt", "w") as somefile:
    somefile.write(text_writing)

        
print()
























