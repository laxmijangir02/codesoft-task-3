import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters to form a password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
8
# Input: Get the desired length of the password from the user
print("Welcome to the Password Generator!")

# Ensure that the user inputs a valid password length
while True:
    try:
        length = int(input("Enter the desired length of your password: "))
        if length < 4:
            print("Password length should be at least 4 characters. Please try again.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer for the password length.")

# Generate and display the password
password = generate_password(length)
print(f"Your generated password is: {password}")
