def fizzbuzz():
    up_till = int(input("Enter a number > "))
    for n in range(1, up_till + 1):
        if n % 3 and n % 5 == 0:
            print(f"{n} FizzBuzz")
        elif n % 5 == 0:
            print(f"{n} Buzz")
        elif n % 3 == 0:
            print(f"{n} Fizz")
        else:
            print(str(n))
            
# fizzbuzz()

#  Write a program that prints number of primes
def find_primes(n):
    primes = []
    num_to_check = 2
    while len(primes) < n:
        found_match = False
        for p in primes: 
            if num_to_check % p == 0:
                found_match = True
                break
        if not found_match:
            primes.append(num_to_check)
        num_to_check += 1
    return primes

print(find_primes(3))

#  Write a program that is a higher lower guessing game
def game():
    n = 42
    i = int(input("What's your guess? > "))
    if i > n:
        print("Too high, try again")
        game()
    elif i < n:
        print("Too low, try again.")
        game()
    else:
        print("You got it!")
        exit()

# game()


