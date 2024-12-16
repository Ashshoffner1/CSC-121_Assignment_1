# Datatypes in Python

# Todo - create a numeric variable called --> var

var = 7

# Describe the data type for this variable
#numarical
#integer
# convert / cast the variable into a decimal with 2 spaces
var_decimal = round(float(var), 2)

# cast float to integer (whole number)

var_integer = int(float(7))

# create a list of numeric values from 1 - 10 and call this list --> list_var

list_var = list(range(1, 10))

# print the first 3 elements of the list
print(list_var[:3])


# tell me the number of elements in this list
num_elements = len(list_var)
print(num_elements)

# print each element in the list created
for elements in list_var:
    print(elements)

# return the 4 element through the 6th element in this list
selected_elements = list_var[3:6]
print(selected_elements)

# put this selected output into a new variable called var_2
var_2 = selected_elements