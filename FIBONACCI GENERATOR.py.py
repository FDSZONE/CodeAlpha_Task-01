def generate_fibonacci(count):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers
    
    # Generate Fibonacci numbers up to the specified count
    while len(fibonacci_sequence) < count:
        # Calculate the next Fibonacci number by summing the last two numbers in the sequence
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        
        # Add the next Fibonacci number to the sequence
        fibonacci_sequence.append(next_fibonacci)
    
    return fibonacci_sequence

# Ask the user for input
count = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = generate_fibonacci(count)
print(f"Fibonacci sequence of {count} numbers:", fibonacci_sequence)
