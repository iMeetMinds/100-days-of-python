
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if not is_prime:
        print("This is not a prime Number")
    else:
        print("This is Prime Number")


n = int(input("Check this number :"))
prime_checker(number = n)