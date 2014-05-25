from operator import mul

def permutations(nlist, m):
    if m == 0:
        yield []
        return

    for list_i in nlist:
        temp = list(nlist)          
        temp.remove(list_i)
        
        for p in permutations(temp, m-1):
            if not [list_i] or not p:
                yield [list_i] + p
            elif [list_i] < p:
                yield [list_i] + p

def get_union_solution(value, percentage):
    all_elements = [round(x * percentage, 11) for x in range(1, value + 1)]
    result = 0.0
    
    result += sum(all_elements)
    
    print '+', all_elements[0], "+", all_elements[1], "+ ... +", all_elements[len(all_elements)-1], "=", result

    for i in range(2, value):
        for x in permutations(all_elements, i):
            s = ''
            result -= round(reduce(mul, x, 1), 11)
            
            s =  '-', str(x[0])
            
            for p in range(1, len(x)):
                s += '*', str(x[p])
            
            print " ".join(s)
    
    intersection = round(reduce(mul, all_elements, 1), 11)
    
    if(value % 2 == 0):
        result -= intersection 
        print '-', all_elements[0], "*", all_elements[1], "* ... *", all_elements[len(all_elements)-1], "=", intersection
    else:
        result += intersection
        print '+', all_elements[0], "*", all_elements[1], "* ... *", all_elements[len(all_elements)-1], "=", intersection    
    
    print '\nResult =', result
    
def get_union(value, percentage):
    all_elements = [x * percentage for x in range(1, value + 1)]
    result = 0.0
    result += sum(all_elements)
    
    for i in range(2, value):
        for x in permutations(all_elements, i):
            result -= reduce(mul, x, 1)
            
    intersection = reduce(mul, all_elements, 1)
    
    if(value % 2 == 0):
        result -= intersection 
    else:
        result += intersection
             
    print '\nResult =', result
    
if __name__ == '__main__':
    get_union_solution(7, 0.01)

