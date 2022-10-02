
from time import sleep

some_count = 100

load = 0
#print(some_count)


for i in range(some_count):
    sleep(0.05)
    
    if i % 10 == 0:
        load += 1

        
    print('Loading: ' + str( int(100/some_count * i))+'%', str('|' * load) , end = '\r')
    
    #print(str( int(100/some_count * i))+'%' , end = '\r')

print('Loading: 100%' , '|' * 10)
print('\a'*3)
print('Complete!')

sleep(2)
