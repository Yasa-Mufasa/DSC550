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
Part 1:

Seeing as sine and cosine are already bound on the y-axis to [0,1] so I don't need to worry about that. Then I just need
to generate the x-values for the interval [0,1]. How many points should I look at? Let's start with 20 points.
'''

x_values = np.arange(0, 1.05, .05)
sine_values = np.sin(x_values)
cosine_values = np.cos(x_values)
sinsin_values = np.sin(sine_values)
coscos_values = np.cos(cosine_values)

# print(sine_values)
# print(cosine_values)
# print(sinsin_values)
# print(coscos_values)
# TODO: Remove comment before turning in.

'''
Alright, all of the values are bound within the [0,1][0,1] bounds. Now I need to get all of these values into a tall
array.
'''

tall_array = np.column_stack((x_values, sine_values, cosine_values, sinsin_values, coscos_values))
# print(tall_array)
# TODO: Remove comment before turning in.

'''
Oh, wait, I went the wrong direction with this. This gives the rows as the different x-values. I need the rows to be the
different functions and the columns the different x-values.
'''

correct_tall_array = np.row_stack((x_values, sine_values, cosine_values, sinsin_values, coscos_values))
print(correct_tall_array)

'''
Hmmm, that's not really much of a tall array, but that answers this portion of the exercise.
'''
