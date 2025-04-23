# Brute force password cracker
# This script attempts to find the original string that corresponds to a given MD5 hash

import hashlib
import itertools
import string
import time

# Target hash
target_hash = "5d41402abc4b2a76b9719d911017c592" # "Hello" for example

# Characters to generate passwords (lowercase letters)
characters = string.ascii_lowercase

# Start the timer
start_time = time.time()

# Attempt brute-force with length up to 5 characters
for length in range(1, 6):
    print(f"Searching for passwords with length {length}...")
    for count, guess in enumerate(itertools.product(characters, repeat=length)):
        guess = ''.join(guess)
        guess_hash = hashlib.md5(guess.encode()).hexdigest()
        
        # Show progress every 100,000 combinations
        if count % 100000 == 0:
            print(f"Checked combinations: {count:,}")
        
        if guess_hash == target_hash:
            end_time = time.time()
            print(f"\nThe original string is: {guess}")
            print(f"Found in {end_time - start_time:.2f} seconds")
            exit()

# If not found
print("The string was not found.")
