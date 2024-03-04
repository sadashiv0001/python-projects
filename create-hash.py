import hashlib

password = "admin@123"
hashed_password = hashlib.sha512(password.encode()).hexdigest()

print("SHA-512:", hashed_password)
