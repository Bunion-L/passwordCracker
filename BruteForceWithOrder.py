import itertools
password = input("Enter the password to crack: ")
passwordLength = int(input("Enter the length of the password as a numeric value to crack: "))
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{}]\|;:,<.>/?'
print(alphabet)
for c in itertools.product(alphabet, repeat=passwordLength):
        guess=''+''.join(c)
        print("Trying " + guess)
        if guess == password:
                print("Password found! it is " + guess)
                break