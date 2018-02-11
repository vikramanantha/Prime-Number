prime = input("What is your whole number?")
prime = int(prime)

for i in range(3, int(prime/2)+1):
    if prime % i == 0:
        input("Your number is not a prime number")
        quit()
input("Your number is a prime number")


