# CodeWars, 5 kyu: "Pete, the baker"
#how many cakes he could bake considering his recipes?

import math

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print('Recipe:')
for item in recipe:
    print(f'{item}: {recipe[item]}')

print('\nAvailable:')
for item in available:
    print(item + ':', available[item])    


def cakes(recipe, available):
    print('\nNums of stuffs: len(recipe) =',len(recipe))

    matches = 0

    count_list = []

    for i in recipe:
        for j in available:
            if i == j:
                print(f'\nrecipe {i} == available {j}')

                c = available[j] / recipe[i]
                c = math.trunc(c)
                
                print('available units per Recipe:', c)

                if c == 0:
                    print('\nImpossible for cooking per Recipe! (not enouf stuff!)')    
                    return 0
                
                count_list.append(c)

                matches += 1


    if matches == len(recipe):
        response = True
        print('\nAll Matches per Recipe:', response)
        count_list = sorted(count_list)

        result = count_list[0]

        print('\nPossible portions for cooking per Recipe:', result)
        
        return result        
        
    else:
        response = False
        print('\nMatches:', response)
        print('Impossible for cooking per Recipe! (missing ingredient!)')        
        
        return 0


cakes(recipe,available)






#print(cakes(recipe,available))



#   Most Clever solution:
def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)



