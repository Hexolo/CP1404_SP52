numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] =[2, 9, 5, 1, 4, 1, 3]
# numbers[3:4] = 1, 5
# 5 in numbers = TRUE
# 7 in numbers = FALSE
# "3" in numbers = FALSE
# numbers + [6, 5, 3] = 3, 1, 4, 1 ,5, 9, 2, 6, 5, 3
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])
numbers[0] = "ten"
print(numbers)
numbers[-1] = 1
print(numbers)
print(numbers[2:6])
print(9 in numbers)
