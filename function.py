# def greet(first_name, last_name):
#    print(f"Salam {first_name} {last_name}")


# greet("Reza", "Seradj")


# def get_greeting(first_name, last_name):
#    return (f"Salam {first_name} {last_name}")


# message = get_greeting("Reza", "Seradj")

# file = open("content.txt", "w")
# file.write(message)

# def increase(number, by=2):
#    return number*by


# print(increase(6, 1))

# def multip(number, by):
#    return number * by


# y = multip(2, 3)
# print(y)


# def multiply(*numbers):
#    total = 1
#    for x in numbers:
#        total = total*x
#    return(total)


# print(multiply(20, 3, 8, 2, 900))

def user_info(**names):
    return(names)


x = user_info(id=1, name="Reza", age=38)
print(x)

# def greet(name):
#     messagage = f"Salam {name}"
#     return messagage


# print(greet("Reza"))
