# def sum(x1, x2):
#     total = x1+x2
#     return total


# def subtract(x1, x2):
#     subt = x1-x2
#     return subt


# def multiply(x1, x2):
#     mulpy = x1*x2
#     return mulpy


# def division(x1, x2):
#     divide = x1/x2
#     return divide


# def reminder(x1, x2):
#     remin = x1 % x2
#     return remin


# def average(x1, x2):
#     ave = (x1+x2)/2
#     return ave


# while True:
#     a = input("x1? or [Q] to Quit ...> ")
#     if a.lower() == "q":
#         break
#     b = input("x2? or [Q] to Quit ...> ")
#     if b.lower() == "q":
#         break
#     x1 = int(a)
#     x2 = int(b)
#     print(f"Sum: {sum(x1, x2)}")
#     print(f"Sub: {subtract(x1, x2)}")
#     print(f"Multiply: {multiply(x1, x2)}")
#     print(f"Division: {division(x1, x2)}")
#     print(f"Reminder: {reminder(x1, x2)}")
#     print(f"Average: {average(x1, x2)}")
#     print("DANI QUE TE PARECE???????")


def sum(x):
    total = 0
    for number in x:
        total += number
    return total


# def subtract(x):
#     total = 0
#     for number in x:
#         total -= number
#     return total


def multiply(x):
    total = 1
    for number in x:
        total *= number
    return total


# def division(x):
#     total = 1
#     for number in x:
#         total /= number
#     return total


# def reminder(x):
#     total = 1
#     for number in x:
#         total %= number
#     return total


# # def average(*x):
# #     total
# #     ave = (x1+x2)/2
# #     return ave

x = []
i = 1
b = input("what is your name? ")
while True:
    while True:

        try:
            a = int(input(f"What is X{i}? [000] to end adding numbers >>"))
        except ValueError:
            print(f"{b}, You did not enter the valid [numerical] value")
            break
        if a == 000:
            break
        x.append(a)
        i += 1
    if a == 000:
        break
print(f"Sum: {sum(x)}")
# print(f"Sub: {subtract(x)}")
print(f"Multiply: {multiply(x)}")
# print(f"Division: {division(x)}")
# print(f"Reminder: {reminder(x)}")
# # print(f"Average: {average(x)}")
# print("Rut te quiero")

print(f'Hola {b} muy bien')
