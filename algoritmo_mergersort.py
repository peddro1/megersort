from random import shuffle
import time
from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
def desenhaGrafico(x,y,y2, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Tempo no caso qualquer")
    ax.plot(x,y2, label = "Tempo na lista invertida")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()


def geraLista(tam):
    
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista
    
    
def geraLista2(tam):
    lista = []
    for i in range(tam-1,0,-1):
        lista.append(i)  
    return lista
    
    
    
x2 = [100000,200000,300000,400000,500000,1000000,2000000]
y = []
y2= []
z = []
z2 = []


def merge_iter(lst1, lst2):
   
    new = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            new += [lst1[0]]
            lst1 = lst1[1:]
        else:
            new += [lst2[0]]
            lst2 = lst2[1:]
    if lst1:
        return new + lst1
    else:
        return new + lst2


def middle(seq):
    return len(seq) // 2

def mergesort_iter(seq):
    
   
    if not seq:
        return []
    if len(seq) == 1:
        return seq
    def helper():
        partition_boundary_list = []
        partition_copy = seq        
        while len(partition_copy) > 1:
            partition_boundary_list +=   [[     [0, middle(partition_copy), False],     [middle(partition_copy), len(partition_copy), False]     ]]
            partition_copy = partition_copy[0:middle(partition_copy)]
        list_index = len(partition_boundary_list) - 1
        left_memoiz = -1
        right_memoiz = -1       
        while partition_boundary_list:
            partition_boundary_element = partition_boundary_list[list_index]
            left_lower, left_upper, sorted_left = partition_boundary_element[0]
            right_lower, right_upper, sorted_right =  partition_boundary_element[1]
            if left_lower == left_memoiz:          
                partition_boundary_list[list_index][0][2] = True
            if right_upper == right_memoiz:        
                partition_boundary_list[list_index][1][2] = True

            if left_upper - left_lower > 1 and  (not partition_boundary_list[list_index][0][2]):
                mid = (left_lower + left_upper) // 2
                partition_boundary_list +=  [[    [left_lower, mid, False],     [mid, left_upper, False]    ]]
                list_index += 1 
            elif right_upper - right_lower > 1 and (not partition_boundary_list[list_index][1][2]):  
                mid = (right_lower + right_upper) // 2
                partition_boundary_list += [[     [right_lower, mid, False],     [mid, right_upper, False]     ]]
                list_index += 1         
            else:
                left_memoiz = left_lower
                right_memoiz = right_upper
                ret_seq = merge_iter(seq[left_lower:left_upper], seq[right_lower:right_upper])
                for element in ret_seq:   
                    seq[left_lower] = element
                    left_lower += 1
                partition_boundary_list.pop(list_index)
                list_index -= 1
   
    helper()
    return  seq
    
    
    
for a in range(len(x2)):
 
    array = (geraLista(x2[a]))
    
    inicio = timeit.default_timer()
    mergesort_iter(array)
    fim = timeit.default_timer()
    
    y.append('%f' %(fim - inicio))
    
    array2 = (geraLista2(x2[a]))
    
    z = timeit.default_timer()
    mergesort_iter(array2)
    w = timeit.default_timer()
    
    y2.append('%f' %(w-z))
    print(y2)
    print(y)
    
desenhaGrafico(x2,y,y2)
