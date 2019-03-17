'''
DSC 550 Data Mining
Exercise 1.2: Create a Search Engine
'''

import numpy as np

'''
Part 1. Evaluate coscos and sinsin on the interval [0,1][0,1] and then stack the results into a tall array with rows
being the (cos(x), sin(x)) (cos(f)(x), sin(f)(x)) entries.

Part 2. Create a random 3x53x5 array using the np.random.rand(3,5) function and compute: the sum of all the entries, the
sum of the rows and the sum of the columns. (Just like sorted had an optional key=arguement, many Numpy functions have
an optional axis=argument!)

Part 3. Create a random 5x55x5 array using the function np.random.rand(5,5). We want to sort the rows accoriding to the
second column. Try combining tarray slicing + argsort + indexing to do this.
'''

'''
Part 1: Evaluate coscos and sinsin on the interval [0,1][0,1] and then stack the results into a tall array with rows
being the (cos(x), sin(x)) (cos(f)(x), sin(f)(x)) entries.

Seeing as sine and cosine are already bound on the y-axis to [0,1] so I don't need to worry about that. Then I just need
to generate the x-values for the interval [0,1]. How many points should I look at? Let's start with 20 points.
'''

x_values = np.arange(0, 1.05, .05)
sine_values = np.sin(x_values)
cosine_values = np.cos(x_values)
sinsin_values = np.sin(sine_values)
coscos_values = np.cos(cosine_values)

print(sine_values)
print(cosine_values)
print(sinsin_values)
print(coscos_values)

'''
Alright, all of the values are bound within the [0,1][0,1] bounds. Now I need to get all of these values into a tall
array.
'''

tall_array = np.column_stack((x_values, sine_values, cosine_values, sinsin_values, coscos_values))
print(tall_array)

'''
Oh, wait, I went the wrong direction with this. This gives the rows as the different x-values. I need the rows to be the
different functions and the columns the different x-values.
'''

correct_tall_array = np.row_stack((x_values, sine_values, cosine_values, sinsin_values, coscos_values))
print(correct_tall_array)

'''
Hmmm, that's not really much of a tall array, but that answers this portion of the exercise.
'''

'''
Part 2:Create a random 3x53x5 array using the np.random.rand(3,5) function and compute: the sum of all the entries, the
sum of the rows and the sum of the columns. (Just like sorted had an optional key=arguement, many Numpy functions have
an optional axis=argument!)

Alright, first thing first is to create the needed array using np.random.rand(3,5)
'''

random_array = np.random.rand(3, 35, 5)
print(random_array)

'''
This creates 3 arrays with 35 rows and 5 columns each. Now to get the sum of all of the entries, the sum of the rows,
and the sum of the columns.
'''

print('The sum of all the entries is: ', np.sum(random_array))
print('The sum of the rows are: ', np.sum(random_array, axis=0))
print('The sum of the columns are: ', np.sum(random_array, axis=1))

'''
Alright, I now have the needed sums for Part 2. That concludes this section of the assignment.
'''

'''
Part 3: Create a random 5x55x5 array using the function np.random.rand(5,5). We want to sort the rows according to the
second column. Try combining array slicing + argsort + indexing to do this.

Hmmmm, well, first thing first is to create the array. Let's start with that.
'''

to_sort = np.random.rand(5, 55, 5)
to_sort = np.round(to_sort, 2)
print(to_sort)

'''
Ok, I have the arrays. I now need to sort them. Let's start by looking at the argsort() function. This probably isn't
the most elegant way of doing this, but this works to sort the array, but doesn't save it back into the array.
'''

for i in range(5):
    sort = to_sort[i]
    sort = sort[np.argsort(sort[:, 1])]
    print(sort)

'''
So how to sort the array and save the results? Why not make a list, store each sorted array in the list, and then use
sorted arrays to make a new array?
'''

sort0 = []
sort1 = []
sort2 = []
sort3 = []
sort4 = []
sorted_list = [sort0, sort1, sort2, sort3, sort4]

for i in range(5):
    sort = to_sort[i]
    sort = sort[np.argsort(sort[:, 1])]
    sorted_list[i] = sort

sorted_array = np.array(sorted_list)
print(sorted_array)
