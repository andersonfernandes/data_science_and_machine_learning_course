number_list = [1,12,10,32,55]

for x in number_list:
    print(x)

# Using ranges
for x in range(1, 12):
    print(x, end=" ")
    if(x % 2 == 0):
        print("is even.")
    else:
        print("is odd.")

# While loop
x = 0
while(x <= 10):
    print(x)
    x += 1
