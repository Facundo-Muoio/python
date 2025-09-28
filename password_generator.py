import re, string, random
 
def password_generator(length = 12, amount_no_chars = 1, amount_numbers = 1, amount_uppercase = 1, amount_lowercase = 1): 
  uppercase = string.ascii_uppercase
  lowercase = string.ascii_lowercase
  digits = string.digits
  symbols = string.punctuation
  all_characters = uppercase + lowercase + digits + symbols
  password = []

  password += random.choices(digits, k=amount_numbers)
  password += random.choices(lowercase, k=amount_lowercase)
  password += random.choices(uppercase, k=amount_uppercase)
  password += random.choices(symbols, k=amount_no_chars)

  remaining = length - len(password)
  password += random.choices(all_characters, k=remaining)

  random.shuffle(password)
  return "".join(password)

password_generator(amount_numbers = 6)

