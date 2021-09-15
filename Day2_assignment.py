# To check the number is prime or not
f = 0
n=int(input("Enter a number: "))
if(n > 1):
    for i in range(2, int((n**(1/2)) + 1)):
        if (n % i == 0):
            f = 1
            break
    if (f == 0):
        print("It is a prime number.")
    else:
        print("It is not a prime number.")
else:
    print("It is not a prime number.")