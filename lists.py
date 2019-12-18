student_grades = [9.1, 8.8, 7.5]

# You can create a list of numbers automatically using a range. For example:

list(range(1, 10))

# That will output:

[1, 2, 3, 4, 5, 6, 7, 8, 9]

# As you can see we just needed to specify the list boundaries inside range(). So, we specified 1and 10. Note that 10 is not included in the list. 
# The generated list always runs up to one number before the upper number. In our example it goes up to 9 since the upper number is 10.

# You can also specify a step as a third argument:

list(range(1, 10, 2))

# That will output:

[1, 3, 5, 7, 9]

# So, the count happens every two items starting from 1 and ending at 9.

>>> list(range(1, 10, 2))
[1, 3, 5, 7, 9]
>>> list(range(1, 10, 5))
[1, 6]
>>> list(range(1, 10, 2))
[1, 3, 5, 7, 9]
>>> list(range(1, 10, 3))
[1, 4, 7]
>>> list(range(1, 100, 4))
[1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97]
>>> list(range(1, 100, 8))
[1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97]
>>> list(range(1, 100, 7))
[1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99]
>>> list(range(0, 100, 7))
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
>>> list(range(0, 100, 8))
[0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]