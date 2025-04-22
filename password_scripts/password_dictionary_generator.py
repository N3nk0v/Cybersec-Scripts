import os
import itertools

def generate_themed_passwords(base_word, max_passwords, output_dir):
    """
    Generates passwords related to a specific theme based on combinations of letters, digits, and special characters.

    :param base_word: The base word (theme) that will be included in the passwords.
    :param max_passwords: The maximum number of passwords to generate.
    :param output_dir: The folder where the dictionary will be saved.
    """
    # Wide alphabet for combinations, including the Bulgarian alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'\",.<>?/|"
    bulgarian_alphabet = "абвгдеёжзиийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    
    # Combine all letters
    full_alphabet = alphabet + bulgarian_alphabet

    # Function to generate word variations
    def generate_word_variations(word):
        substitutions = {
            "a": ["@", "4", "A"],
            "s": ["$", "5", "S"],
            "o": ["0", "O"],
            "i": ["1", "!", "I"],
            "e": ["3", "E"],
            "c": ["(", "<", "C"],
            "к": ["<", "К"],  # Example substitution for a Bulgarian letter
            "е": ["3", "Е"]
        }
        variants = set()
        # Generate all combinations of lowercase/uppercase letters
        variants.update("".join(x) for x in itertools.product(*((c.lower(), c.upper()) for c in word)))
        # Replace letters with special characters or similar symbols
        for i, char in enumerate(word):
            if char in substitutions:
                for sub in substitutions[char]:
                    variant = word[:i] + sub + word[i + 1:]
                    variants.add(variant)
        return variants

    # Check and create the directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Determine the next file name
    existing_files = [f for f in os.listdir(output_dir) if f.startswith("dictionary") and f.endswith(".txt")]
    next_index = len(existing_files) + 1
    file_name = os.path.join(output_dir, f"dictionary{next_index:02d}.txt")

    # Write passwords directly to a file
    with open(file_name, "w", encoding="utf-8") as file:
        count = 0
        base_variants = generate_word_variations(base_word)  # Variations of the base word

        # First, write the variations of the base word
        for variant in base_variants:
            if count >= max_passwords:
                break
            file.write(variant + "\n")
            count += 1

        # Generate passwords for the theme (with a limited number of combinations)
        # Generate combinations with more limited character lengths
        for length in range(8, 15):  # Change the length range: from 8 to 14 characters
            for combination in itertools.product(full_alphabet, repeat=length):
                if count >= max_passwords:
                    break
                word_combo = ''.join(combination)
                # Combine the combinations with the thematic words
                if base_word in word_combo:
                    file.write(word_combo + "\n")
                    count += 1
            if count >= max_passwords:
                break

    print(f"The dictionary is saved in {file_name} with {count} passwords.")

# Example usage
if __name__ == "__main__":
    generate_themed_passwords(
        base_word="medic", 
        max_passwords=1000,  
        output_dir="D:\\python_projects\\Dictionary Generator"
    )
