# Password Scripts Collection
This folder contains a collection of scripts related to password cracking, password analysis, and password security.
---

🔐 check_password
This script helps users evaluate the security of their passwords by performing both local and online checks, along with password strength analysis.

Features:
Local Check: The script checks if the password is present in a predefined password dictionary file (such as rockyou.txt).
Online Check: It also queries the HaveIBeenPwned (HIBP) service using the k-anonymity model to verify if the password has been exposed in any public data breaches.

Password Strength Analysis: It evaluates password strength based on the following criteria:
Minimum length: 12 characters for medium strength, longer than 16 for strong. Contains uppercase and lowercase letters.
Includes at least one digit and one special character (e.g., !@#$%^&*).
Strong passwords must meet all these conditions and exceed 16 characters.
                                                       
User Interaction:
The user is prompted to input a password, after which the script provides feedback on:
Password strength (Strong, Medium, Weak).
                                                       
Exposure check:
If it exists in a dictionary file locally.
If it has been exposed in public breaches via HIBP.

How to Use:
Choose Option: Select whether to check the password locally (using a dictionary) or online (via HIBP).
Input Password: Enter the password to evaluate.
View Results: Receive feedback on password strength and exposure status.
Repeat: Option to check more passwords.
This tool is intended to help improve password security by identifying weak or compromised passwords.

 🔑 Password Dictionary Generator Script

### Description:
This script generates a customized password dictionary based on a base word (theme) and creates variations of that word using combinations of letters, digits, and special characters. 
It also supports generating themed passwords with a mix of different character sets, including the Bulgarian alphabet. 
The generated passwords are saved in a text file within the specified output directory.

### Key Features:
- **Base Word Variations:** The script generates password variations based on a given base word, replacing characters with similar-looking characters (e.g., "a" with "@", "s" with "$").
- **Wide Alphabet Support:** It supports a wide alphabet, including both the English and Bulgarian alphabets, as well as digits and special characters.
- **Password Length Control:** The script generates passwords of varying lengths, with an option to control the range of lengths (between 8 and 14 characters in this case).
- **Output:** The generated passwords are written into a text file in the output directory, with a filename that increments for each new dictionary generated.

### Usage Example:
To generate a dictionary for the theme "medic" for example, with a maximum of 1000 passwords, run the script, and the resulting dictionary file will be saved in the specified output directory.

🔐 MD5 Hash Brute-force Script
📄 Script: md5_bruteforce.py
🧠 Description
This is a simple brute-force tool for cracking MD5 hashes, written in pure Python. It attempts to recover the original plaintext string that corresponds to a given MD5 hash by generating and checking all possible combinations of lowercase letters, up to a specified length.

⚙️ How It Works
Uses itertools.product to generate combinations of characters.
Hashes each combination using hashlib.md5().
Compares each generated hash to the target hash.
If a match is found, prints the original string and time taken.

🧪  For Example when we input target hash:
target_hash = "5d41402abc4b2a76b9719d911017c592" it shoud shows us "hello"

⚠️ Disclaimer
All scripts in this folder are part of my personal learning journey in cybersecurity and are created solely for educational and academic purposes.




                                                       
