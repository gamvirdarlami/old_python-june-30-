for i in range(1,101):
    if i % 3 == 0 and i % 5 ==0:
        print(f"Fizzbuzz: {i}")
    if i % 3 == 0:
        print(f"Fizz: {i}")
    elif i % 5 == 0:
        print(f"buzz: {i}")