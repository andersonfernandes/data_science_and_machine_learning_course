numbers_list = [1,2,3,4,5,6]

for number in numbers_list:
    print(number, end=" ")
    if(number % 2 == 0):
        print("is even.")
    else:
        print("is odd.")
