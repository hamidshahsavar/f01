import random

secret = random.randint(50, 100)

while True:
    num = int(input("adado bego : "))


    if num > secret:
        print("ziaad gofti")
    elif num < secret:
        print("kame kame bishtaresh kon")
    elif num == secret:
        print("jon kandia vali dorose")
        break


