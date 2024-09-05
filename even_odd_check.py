"""Simple python project that checks if a certain list elements are even or odd
the list is taken as an input according to its length
the even nums are copied to an even called list
the odd nums are copied to an odd called list
 """

numbers = []
total = int(input("How many items do you have?"))

# There are three different ways to take the list as an input & all of them are doing the same task

# for i in range(total):
#     answer = int(input("Enter : "))
#     numbers.append(answer)

count = 0
# while count < total:
#     answer = int(input("ENTER : "))
#     numbers.append(answer)
#     count += 1

while True:
    if count < total:
        answer = int(input("enter : "))
        numbers.append(answer)
    elif count == total:
        break
    count = count + 1

print("Your list is : ", format(numbers))


even = []
odd = []
#2 different ways to loop the list elements
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         even.append(numbers[i])
#     else :
#         odd.append(numbers[i])

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even nums are : " + str(even))
print("odd nums are : " + str(odd))



