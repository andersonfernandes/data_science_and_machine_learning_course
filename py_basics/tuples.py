# Tuples are imutable lists
x = (5,2,12)
print(x)
print("Length of the tuple:", len(x))

# Lists of tuples
y = (6,1,10)
l = [x, y]
print(l)

# Using with assignemt from a string split
(name, age) = "John,32".split(',')
print("Name:", name)
print("Age:", age)
