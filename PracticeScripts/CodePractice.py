###BASICS###
"""
    Python is 0 indexed
    Tabs represent blocks of code.
"""
# Declaring multiple variables
hello, world = "Hello", "World"

# Declaring floats
fl = float(2)

# If/else
n = 0
if n == 1:
    print("Hello, World!")
else:
    # Number to string & multiple prints
    print(hello + " " + world + ":" + str(fl))

    # Print statements
    lst = [1, 2, 3]
    print("H: %s, W: %s, F: %0.2f" % (hello, world, fl))
    print("With Format: %s" % hello)
    print(hello + " " + world, fl)
    print("A list: %s" % lst)


print("________________________________________")


# LISTS

# List
myList = ["lets", "get", "it"]

# Tuple - heterogeneous values can be contained
myTuple = ("lets", "get", 1, "icecream")

result = ""
myList.append("done")

for data in myList:
    result += data + ", "

print(myList+myList)
print("Cmon, %s %s only %d %s" % myTuple)
print("ListSize: %d" % len(myList))
print(myList[0])
print(result)


print("________________________________________")


# OPERATORS
numList_Prod = [1, 2, 3] * 2
numList_Append = [1, 2] + [3, 4]
print("11%3:", 11%3)
print("1 + 2 * 3 / 4.0: ", 1 + 2 * 3 / 4.0)
print("Seven Square: %d" % 7 ** 2)
print("Seven Cube: %d" % 7 ** 3)
print("Five Hello's: %s" % ("hello " * 5))
print("[1, 2, 3] * 2: ", numList_Prod)
print("[1, 2] + [3, 4]: ", numList_Append)


print("________________________________________")

# STRING OPERATIONS
"""
    All operations are 0 indexed
    All operations are case sensitive
"""
astring = "HelloWorld!"
print("TESTING WITH STRING: %s" % astring)
print("Length of string; len(string): %d" % len(astring))
print("First Index of X; string.index('o'): %d" % astring.index('o'))
print("Count character occurrences; string.count('x'): %d" % astring.count('l'))
print("Count character occurrences; string.count('X'): %d" % astring.count('L'))
print("Char at index i; string[1]: %s" % astring[1])
print("Substring from index i inclusive to j-1 inclusive; string[2:4]: %s" % astring[2:4])
print("Substring from index i to end; string[i:]: %s" % astring[2:])
print("Step over characters; string[start:stop:step]: %s" % astring[1::2])
print("Reverse string; string[::-1]: %s" % astring[::-1])
print("Uppercase; string.upper(): %s" % astring.upper())
print("Lowercase; string.lower(): %s" % astring.lower())
print("StartsWith; string.startswith('he'): %s" % astring.startswith("He"))
print("EndsWith; string.endswith('LD!'): %s" % astring.endswith("LD!"))
print("Split; string.split('o'): %s" % astring.split('o'))



print("________________________________________")

# CONDITIONS

if 1 == 2 or 3 == 3:
    print("OrCondition")
"""elif 1 == 1 and 2 == 2:
    print("AndCondition")
"""

eString = ""
eList = []
eNumber = 0

if not eString:
    print("Empty string is false")
if not eList:
    print("Empty list is false")
if not eNumber:
    print("Number 0 is false")

"""
    'in' operator checks for a value in a list
    
    name = "John"
    if name in ["John", "Rick"]:
        print("Your name is either John or Rick.")
        
    'is' operator checks for object equivalence not values
    
    x = [1,2,3]
    y = [1,2,3]
    print(x == y) # Prints out True
    print(x is y) # Prints out False
"""



print("________________________________________")

# LOOPS
"""
    Keywords 'break' and 'continue' function as expected. 
"""
y = [1, 9, 10]
for x in y:
    print(x, end=" ")
print("")
for x in range(5):
    print(x, end=" ")
print("")
# start index, end index, step
for x in range(2, 10, 2):
    print(x, end=" ")
print("")
for x in range(10, 2, -1):
    print(x, end=" ")
print("")

"""
    else condition in loops executes only if loop condition fails
    if loop is broken out of due to 'break' statement, else does not execute
"""

x = 10
while x < 10:
    print("x is less than 10")
    x += 1
else:
    print("x was never less than 10")




print("________________________________________")