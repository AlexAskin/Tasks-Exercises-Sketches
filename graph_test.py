graph = {}


graph["you"] = [

"alice",
"bob",
"claire",

]

print(graph)
print()

graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom","jonny"]


graph["anuj"] = ['you']
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = []


for i in graph:
    print(i + ': ' + str(graph[i]))

def mango_seller():
    mango_seller = 'jonny'
    return mango_seller

#print(mango_seller())
if 'jonny' == mango_seller(): print('Ok')


from collections import deque

s_queue = deque()

print(s_queue)

s_queue += graph["you"]

print(len(s_queue), s_queue)



def Checker(s_queue):
    checked_persons = []
    while s_queue: # пока очередь не пуста
        
        person = s_queue.popleft()  # извлекается первый человек
        print(person)

        if person not in checked_persons:
            if person == mango_seller():
                print(f'\n{person} is a mango seller!')
                return True
            else:
                s_queue += graph[person]
                checked_persons.append(person)
                
            
    print('\nMango seller is not Found!')
    return False


Checker(s_queue)


