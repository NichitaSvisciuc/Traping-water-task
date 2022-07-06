import numpy as np

from collections import defaultdict


def divide(array, index_iterator_length):

    divided_array = []
    array_of_divided_arrays = []

    # Adding only first level because the code below starts from 2nd due to its specifics

    for i in range(len(array)):
      if array[i] > 0:
        divided_array.append(1)
      else:
        divided_array.append(0)

    array_of_divided_arrays.append(divided_array)
    divided_array = []

    # Array divisation from 2nd level to next ones

    for iterator in range(index_iterator_length - 1):
      for i in range(len(array)):
        if array[i] > 0:
          if array[i] == 1:
            array[i] -= 1
            divided_array.append(0)
          else:

            divided_array.append(1)
            array[i] -= 1
        else:

          divided_array.append(0)
      array_of_divided_arrays.append(divided_array)
      divided_array = []

    return array_of_divided_arrays

def stripArray(array):

    for i in range(len(array)):
      if array[i] == 1:
        break
      else:
        array[i] = ''

    for i in range(len(array))[::-1]:
      if array[i] == 1:
        break
      else:
        array[i] = ''

    return array

def calculateDistance(array):

    k = 0

    for i in range(len(array)):
      striped_array = stripArray(array[i])

      for j in range(len(striped_array)):
        if striped_array[j] == 0:
          k += 1

    return k

test_array_1 = [4,2,0,3,2,5]
test_array_2 = [0,1,0,2,1,0,1,3,2,1,2,1]

divided_array_1 = divide(test_array_1, np.amax(test_array_1))
divided_array_2 = divide(test_array_2, np.amax(test_array_2))

print(calculateDistance(divided_array_1))
print(calculateDistance(divided_array_2))
