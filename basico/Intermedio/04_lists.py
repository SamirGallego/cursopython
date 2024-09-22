numbers = []
for element in range(1,11):
  numbers.append(element*2)

print(numbers)

numbers_v2= [element for element in range(3,11000) if element%(element-1) == 2]
print(numbers_v2)