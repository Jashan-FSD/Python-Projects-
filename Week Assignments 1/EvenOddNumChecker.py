# Function to check Even or Odd
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

# Function to check Prime Number
def check_prime(num):
    if num <= 1:
        print(num, "is not a Prime Number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a Prime Number")
                return
        print(num, "is a Prime Number")

# Main Program
num = int(input("Enter a number: "))

check_even_odd(num)
check_prime(num)