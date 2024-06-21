import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all the allowed characters
    all_chars = lowercase + uppercase + digits + special_chars
    
    # Ensure there are characters to choose from
    if not all_chars:
        raise ValueError("No characters available to generate a password. Check your settings.")
    
    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

# Customize your password settings
password_length = 12
include_uppercase = True
include_digits = True
include_special_chars = True

# Generate the password
password = generate_password(password_length, include_uppercase, include_digits, include_special_chars)
print(f"Generated Password: {password}")
