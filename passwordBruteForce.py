import random
import string

def crack_password(password):
    attempts = 0 #recordes how many attemtps it took
    while True:
        guess = ''.join(random.choices(string.ascii_letters + string.digits, k=len(password))) #selects a random combination of letters and numbers
        attempts += 1
        if guess == password: #compares guess to the inputed password
            return attempts

password = input("Enter the password to crack: ") #takes user input

print ("Cracking password...")

attempts = crack_password(password)

print(f"The password was cracked in {attempts} attempts.") #returns number of attempts when password is cracked