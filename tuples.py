
# tuple is just like a list but without square brackets!
# main difference is that tuples are immutables - lists are not.

# basically - tuples you cannot change (add/remove etc) 
# lists you can change...(add/remove etc)

#this is a tuple
monday_temperatures = {1, 4, 5}

# this is a list
list_temperatures = [1, 4, 5]

# you can add to lists
list_temperatures.append(6)

print(list_temperatures)
print(monday_temperatures)

# you cannot append to tuples - you get an error (there is no append method):
monday_temperatures.append(6)

# similarly tuples do not have a remove method as well
monday_temperatures.remove(4)

# three tuples as lists inside of it
color_codes = {(1,2,3),(4,5,6),(7,8,9)}