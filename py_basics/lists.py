x = [112,15,180,555,31]
print("List size:", len(x))

print("First 3 elements:", x[:3])

print("Elements starting from the third position:", x[3:])

print("Last 3 elements:", x[-3:])

# Inserting new elements
x.append(1)

# Concatenating lists without modify the original ones
y = [44,66,88]
print(x + y)
print(x)
print(y)

# Concatenating lists modifying the original ones
x.extend(y)
print(x)

# List of lists
z = [100,200,300]
a = [y, z]
print(a)

# Sorting a list
x.sort()
print(x)

# Reverse sorting a list
x.sort(reverse=True)
print(x)
