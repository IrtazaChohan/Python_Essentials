#python essentials notes - Shift+Enter to run each line (like F8 in powershell ise)

type(10)

# get list of all built in functions in python
dir(__builtins__)

# Ctrl L to clear the screen in bash

int(10.5)
int(10.6)
round(10.6)
float(10)
int("100")
int("100") + 100
float("100.10")
str(10)
str("10.09")

help(len)

address = ["Flat Floor Street","18","New York"]
address[0] + " " + address[1]

#shows the lengh of the list..ie 3 items
len(address)

"Hello"[1]
"Helllo World"[5]
print("Hello", "Hi")

address[1]
int(address[1]) + 20 
type(address[1])
address[-1]
address[-2]

#slicing - slicing is upper bounds exclusive
# this ignores the last item but gives you the first and secnd item
address[0:2]

# all items of the list
address[0:]

# Or..all list items
address[:]

#get everything from start to index 2
address[:2]

# this gives an empty list since slicing goes left to right and not the other way round
address[-1:-2]

#this works though:
address[-2:

# you get 18 since slicing is upper bound exclusive
address[-2:-1]

# shows all the methods that you can apply to the function
dir(address)

dir(str)
dir(list)

# now to apply any of the methods:
address.append("USA")

print(address)
address

address.remove("USA")

# remove based on index (will show you what it removed):
address.pop(1)

#shows help for the method
help(list.reverse)

#dictionary - contains multiple values - KEY/PAIR relationship:
# python LISTS contain one value however dictionary contain two values
pins = {"Mike":1234,"Joe":1111,"Jack":2222}

# indexing on dictionary does not work
pins[0]

#But you can call individual information - it will gives you the value of the key
pins["Mike"]

#shows it as a int (since the value it returns is an int)
type(pins["Mike"])

