def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def get_user_choice():
    """Get user's choice for prime number finding method."""
    print("\nPrime Number Finder")
    print("1. Check if a single number is prime")
    print("2. Find all primes in a range")
    print("3. Find first N prime numbers")
    print("4. Exit")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid integer.")

def check_single_number():
    """Check if a single number is prime."""
    try:
        num = int(input("Enter a number to check: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")

def find_primes_range():
    """Find primes in a user-specified range."""
    try:
        start = int(input("Enter the start of range: "))
        end = int(input("Enter the end of range: "))
        
        if start > end:
            print("Start should be less than or equal to end.")
            return
        
        primes = find_primes_in_range(start, end)
        
        if primes:
            print(f"Prime numbers between {start} and {end}:")
            print(primes)
            print(f"Total count: {len(primes)}")
        else:
            print(f"No prime numbers found between {start} and {end}.")
            
    except ValueError:
        print("Please enter valid integers.")

def find_first_n_primes():
    """Find the first N prime numbers."""
    try:
        n = int(input("How many prime numbers do you want? "))
        if n <= 0:
            print("Please enter a positive number.")
            return
        
        primes = []
        num = 2
        
        while len(primes) < n:
            if is_prime(num):
                primes.append(num)
            num += 1
        
        print(f"First {n} prime numbers:")
        print(primes)
        
    except ValueError:
        print("Please enter a valid integer.")

def main():
    """Main function to run the prime number finder."""
    while True:
        choice = get_user_choice()
        
        if choice == 1:
            check_single_number()
        elif choice == 2:
            find_primes_range()
        elif choice == 3:
            find_first_n_primes()
        elif choice == 4:
            print("Thank you for using Prime Number Finder!")
            break
        
        print("\n" + "-" * 40)

if __name__ == "__main__":
    main()
