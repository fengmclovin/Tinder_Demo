import secrets
import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)

    def hash_password(self, password):
        # Generate a salt for hashing
        salt = secrets.token_hex(16)

        # Hash the password using SHA-256 and salt
        hash_obj = hashlib.sha256()
        hash_obj.update((password + salt).encode('utf-8'))
        return salt + hash_obj.hexdigest()

    def verify_password(self, password):
        # Extract the salt from the stored password hash
        salt = self.password_hash[:32]

        # Hash the provided password with the extracted salt
        hash_obj = hashlib.sha256()
        hash_obj.update((password + salt).encode('utf-8'))
        new_hash = salt + hash_obj.hexdigest()

        # Compare the hashed passwords
        return new_hash == self.password_hash

# Example usage:
username = "example_user"
password = "SecurePassword123!"

# Create a user instance
user = User(username, password)

# Verify password
print("Password verification:", user.verify_password(password))  # Output: True

# Demonstrate secure storage (not recommended for production, use environment variables or secure storage solutions)
secure_storage = {}
secure_storage[username] = user.password_hash

# Access stored password hash securely
stored_hash = secure_storage.get(username)
print("Stored password hash:", stored_hash)

# Attempt to verify password using stored hash
print("Verification using stored hash:", user.verify_password(password))  # Output: True
