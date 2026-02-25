def power8(number):
    if number == 0:
        return False
    
    while number % 8 == 0:
        number = number // 8
    return number == 1

number = int(input("Enter a number: "))
if power8(number):
    print(number, "is a power of 8.")
else:
    print(number, "is not a power of 8.")