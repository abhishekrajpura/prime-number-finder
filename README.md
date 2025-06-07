# Prime Number Finder

A comprehensive Python program that provides multiple ways to work with prime numbers.

## Features

- **Check Single Number**: Verify if a specific number is prime
- **Range Search**: Find all prime numbers within a given range
- **First N Primes**: Generate the first N prime numbers
- **Optimized Algorithm**: Uses efficient prime checking with O(√n) complexity
- **Input Validation**: Handles invalid inputs gracefully
- **User-Friendly Interface**: Interactive menu system

## Usage

### Running the Program

```bash
python prime_finder.py
```

### Menu Options

1. **Check if a single number is prime**
   - Enter any integer to check if it's prime
   - Example: Input `17` → Output: "17 is a prime number."

2. **Find all primes in a range**
   - Enter start and end values
   - Example: Range 10-30 → Output: [11, 13, 17, 19, 23, 29]

3. **Find first N prime numbers**
   - Enter how many primes you want
   - Example: First 5 primes → Output: [2, 3, 5, 7, 11]

4. **Exit**
   - Quit the program

## Algorithm Details

### Prime Checking Algorithm
- **Time Complexity**: O(√n) for each number
- **Space Complexity**: O(1) for checking, O(k) for storing results
- **Optimization**: Only checks odd divisors after eliminating even numbers

### Example Output

```
Prime Number Finder
1. Check if a single number is prime
2. Find all primes in a range
3. Find first N prime numbers
4. Exit
Enter your choice (1-4): 2
Enter the start of range: 10
Enter the end of range: 30
Prime numbers between 10 and 30:
[11, 13, 17, 19, 23, 29]
Total count: 6
```

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abhishekrajpura/prime-number-finder.git
   ```

2. Navigate to the directory:
   ```bash
   cd prime-number-finder
   ```

3. Run the program:
   ```bash
   python prime_finder.py
   ```

## Code Structure

- `is_prime(n)`: Core function to check if a number is prime
- `find_primes_in_range(start, end)`: Find all primes in a given range
- `get_user_choice()`: Handle user menu selection
- `check_single_number()`: Handle single number prime checking
- `find_primes_range()`: Handle range-based prime finding
- `find_first_n_primes()`: Handle finding first N primes
- `main()`: Main program loop

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.
