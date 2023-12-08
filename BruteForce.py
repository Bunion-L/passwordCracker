import random
import string

def crack_password(password):
    #recordes how many attemtps it took
    attempts = 0 
    while True:
        #selects a random combination of letters and numbers
        guess = ''.join(random.choices(string.ascii_letters + string.digits, k=len(password))) 
        attempts += 1
        #compares guess to the inputed password
        if guess == password: 
            return attempts

#takes user input
password = input("Enter the password to crack: ") 

print ("Cracking password...")

attempts = crack_password(password)

#returns number of attempts when password is cracked
print(f"The password was cracked in {attempts} attempts.") 