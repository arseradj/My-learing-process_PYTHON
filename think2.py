result = 2+3*5
name = input("What's your name? ")
i = 1
while True:
    print(f'Attempt {i}', "."*i)
    message = int(
        input(f"Tell me {name}, What is the product of 2+3*5? [000] if you give up!!! "))
    if message == 000:
        print(f'{name}, hey you gave up after {i} attempt(s), try later ..')
        break
    if result != message:
        print(f"You have failed at the Attempt #{i}, try again {name}", "."*i)
        i += 1
    if result == message:
        print(f"Well done {name}, you're smart!")
        break
