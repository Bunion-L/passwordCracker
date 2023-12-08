import itertools
#takeks the password to crack
password = input("Enter the password to crack: ")
#takes password length as a number
passwordLength = int(input("Enter the length of the password as a numeric value to crack: "))
#stores every combination of letters, numbers, and symbols
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{}]\|;:,<.>/?'
print(alphabet)
#prints every combination and compares them
for c in itertools.product(alphabet, repeat=passwordLength):
        guess=''+''.join(c)
        print("Trying " + guess)
        #compares guess to password
        if guess == password:
                print("Password found! it is " + guess)
                break