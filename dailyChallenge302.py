unsorted = [1,4,6,0,75,35,2,3,5,456,34,5,3,243,345,456,3,34,34,34,1,12,32,3,345,456,23,234,1]
from random import randint

from matplotlib import pyplot as plt

def array_creator(N):
    array = []
    for i in range(N):
        array.append(randint(0,N))
    return array


def flipfront(array,n):
    array[0:n] = reversed(array[0:n])
    return array

print(unsorted)

def flip_sort(array):

    max_element = max(array)
    index_element = array.index(max_element)
    flipfront(array,index_element+1)
    flipfront(array,len(array))

    for i in range(1,len(array)):
        max_element = max(array[0:-i])
        index_element = array[0:-i].index(max_element)
        flipfront(array,index_element+1)
        flipfront(array,len(array)-i)
    return array

array_length = 20000
#print(flip_sort(array_creator(array_length)))
x = [i for i in range(array_length)]
plt.plot(x,array_creator(array_length))
