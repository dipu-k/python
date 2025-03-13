
import random
import string
import time
def generate_password(length):
  # Generate a random password of the given length
  password = ""
  for i in range(length):
    # Generate a random character and add it to the password
    password += random.choice(string.ascii_letters + string.digits + string.punctuation)
  return password

# Test the function
password = generate_password(10)
print(password)