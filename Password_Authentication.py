# Code for Basic Passwrod Authentication
"""import getpass

database = {"Rakib": "123", "Shaikat": "456"}

username = input("Enter the username: ")

password = getpass.getpass("Enter the password: ")

for i in database.keys():
    if username == i:
        while password !=database.get(i):
            password = getpass.getpass("Enter the password again: ")

        break
print("Verified")"""

# Modeified Code for Passwrod_Authentication
"""import getpass

# Simulating a secure hashed password database
database = {"Rakib": "123", "Shaikat": "456"}  # Replace with hashed passwords in real scenarios.

username = input("Enter the username: ")

if username in database:
    # Password prompt
    password = getpass.getpass("Enter the password: ")
    # Validate the password
    while password != database[username]:
        print("Incorrect password. Try again.")
        password = getpass.getpass("Enter the password again: ")
    print("Verified")
else:
    print("Username not found.")"""


# Code for Passwrod Authentication(Use bcrypt)

import bcrypt
import getpass

# Simulated database with hashed passwords
def initialize_database():
    """Initialize a secure database with hashed passwords."""
    database = {
        "Rakib": bcrypt.hashpw("123".encode(), bcrypt.gensalt()),
        "Shaikat": bcrypt.hashpw("456".encode(), bcrypt.gensalt())
    }
    return database

# Authenticate user
def authenticate_user(database):
    """Authenticate a user by username and password."""
    username = input("Enter the username: ")
    
    # Check if username exists
    if username not in database:
        print("Error: Username not found.")
        return False

    # Prompt for password securely
    password = getpass.getpass("Enter the password: ")

    # Verify the hashed password
    if bcrypt.checkpw(password.encode(), database[username]):
        print("Verified: Access Granted!")
        return True
    else:
        print("Error: Incorrect password.")
        return False

# Main Program
if __name__ == "__main__":
    user_database = initialize_database()  # Initialize database with hashed passwords
    if authenticate_user(user_database):
        print("Welcome to the system!")
    else:
        print("Authentication failed.")
