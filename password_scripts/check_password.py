"""
Password Security Checker Script

This script allows you to check the security of a password in two ways:
1. Local check using a dictionary file (e.g., rockyou.txt) – verifies if the password exists in a predefined password dictionary.
2. Online check via HaveIBeenPwned (HIBP) – checks whether the password has been exposed in known data breaches using the k-anonymity model.

Additionally, the script checks the strength of the password based on several criteria:
- Minimum length of 12 characters (for medium strength).
- Contains both uppercase and lowercase letters.
- Includes at least one digit and one special character (e.g., !@#$%^&*).
- Strong passwords must meet all these conditions and be longer than 16 characters.

The user is prompted to input a password, and the script performs the necessary checks based on the user's choice, providing feedback on password strength and exposure.

The user can choose to check additional passwords until they decide to stop.

"""

import os
import hashlib
import requests
import re

def load_dictionary(dict_path):
    if not os.path.exists(dict_path):
        print(f"❌ File {dict_path} does not exist.")
        return set()

    with open(dict_path, 'r', encoding='utf-8', errors='ignore') as file:
        return set(line.strip() for line in file)

def check_password_in_dict(password, password_set):
    return password in password_set

def check_password_online(password):
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1pwd[:5]
    suffix = sha1pwd[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    if res.status_code != 200:
        print("⚠️ Error connecting to HIBP.")
        return -1

    hashes = (line.split(':') for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

def check_password_strength(password):
    """Check the strength of the password with detailed criteria."""
    
    length_criteria = len(password) >= 12  # Length check (at least 12 chars for medium strength)
    upper_criteria = re.search(r'[A-Z]', password)  # Uppercase letters
    lower_criteria = re.search(r'[a-z]', password)  # Lowercase letters
    digit_criteria = re.search(r'\d', password)  # Numbers
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>€§]', password)  # Special characters
    mixed_case_criteria = upper_criteria and lower_criteria  # Combination of both cases
    number_and_special_criteria = digit_criteria and special_char_criteria  # Combination of numbers and special chars

    # Strong password: All criteria met, and length > 16 chars
    if length_criteria and mixed_case_criteria and digit_criteria and special_char_criteria and len(password) > 16:
        return "Strong"
    # Medium password: All basic criteria met (length, mixed case, numbers, or special chars)
    elif length_criteria and mixed_case_criteria and (digit_criteria or special_char_criteria):
        return "Medium"
    # Weak password: If any basic criteria are missing (length, mixed case, digits, or special chars)
    else:
        return "Weak"

def main():
    print("=== Password Security Checker ===")

    while True:  # Loop for checking multiple passwords
        print("1. Local check using a dictionary")
        print("2. Online check via HIBP (anonymous)")
        choice = input("Choose option (1 or 2): ").strip()

        if choice not in ['1', '2']:
            print("❌ Invalid choice.")
            continue

        password = input("🔑 Enter the password you want to check: ")

        # Password strength - Check
        strength = check_password_strength(password)
        print(f"🔒 Password strength: {strength}")

        if choice == '1':
            dictionary_path = "D:\\rockyou.txt"  # Dictionary path
            print(f"\n🔍 Checking locally using dictionary: {dictionary_path}...")
            password_dict = load_dictionary(dictionary_path)

            if not password_dict:
                print("⚠️ Dictionary not loaded. Please check the path.")
                continue

            if check_password_in_dict(password, password_dict):
                print("⚠️ This password was found in the dictionary! Choose a more secure one.")
            else:
                print("✅ The password was not found in the dictionary.")
        
        elif choice == '2':
            print("\n🌐 Checking online via HaveIBeenPwned...")
            count = check_password_online(password)
            if count == -1:
                print("⚠️ Error communicating with HIBP.")
            elif count > 0:
                print(f"⚠️ This password has been found {count} times in public breaches!")
            else:
                print("✅ The password was not found in HIBP’s breach database.")

        # Ask user if they want to check another password
        repeat = input("\nDo you want to check another password? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
