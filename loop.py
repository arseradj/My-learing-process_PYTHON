# for x in range(3):
#    print("Attempt", x+1, (x+1)*".")
# for number in range(1, 4):
#    print("Attempt", number, number*".")
# Successful = False
# for number in range(1, 4):
#    print("Attemp", number, number*".")
#    if Successful:
#        print("Attempt is done successfully")
#        break
# else:
#    print("Attemps were not successfull")
# for x in range(1, 4):
#    for y in range(1, 10):
#        print(f"({x}, {y})")
# for x in "python":
#    print(x*2)
# command = ""
# while command.lower() != "quit":
#    command = input(">")
#    print("ECHO", command)
# while True:
#    command = input(">")
#    print("Echo", command)
#    if command.lower() == "quit":
#        break
# for x in [2, 4, 6, 8]:
#    print(x)
# print("We have 4 even numbers")
# for x in [1, 3, 5, 7]:
#    print(x+1)
# print("We have 4 even numbers")
# count = 0
# for x in range(1, 10):
#    if x % 2 == 0:
#        print(x)
#        count += 1
# print(f"We have {count} even numbers")
# answer = 4
# attempt = 0
# while attempt < 3:
#    x = int(input("what is 2+2? "))
#    if x != answer:
#        print("failed!")
#        attempt += 1
#    else:
#        print("well done")
#        break
# answer = 4
# for number in range(3):
#    x = int(input("what is 2+2? "))
#    if x != answer:
#        print("failed!")
#    else:
#        print("well done")
#        break
# out = ""
# for x in (5, 2, 5, 2, 2):
#    out = ""
#    for count in range(x):
#        out += "x"
#    print(out)


# def deb(*numbers):
#     for x in numbers:
#         out = f"{x}"
#         for count in range(x):
#             out += "C"
#         print(out)


# n = deb(5, 2, 5, 2, 2)
# print(n)
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return ("fizzbuzz")
    if input % 3 == 0:
        return ("fizz")
    if input % 5 == 0:
        return ("buzz")
    return input


print(fizz_buzz(35))
