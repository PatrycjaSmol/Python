import sys
import random
import string 

password = []
characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left
    
    if number_of_characters < 0 or number_of_characters > characters_left:
        print ("Wybrana ilość znaków jest spoza dostępnego przedziału. Spróbuj jeszcze raz.", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("Pozostało znaków:", characters_left)
password_length = int(input("Podaj długość wygenerowanego hasła: "))

if password_length < 8:
    print("Hasło musi mieć conajmniej 8 znaków. Spróbuj jeszcze raz.")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input("Ile małych liter ma mieć hasło? "))
update_characters_left(lowercase_letters)

uppercase_letters = int(input("Ile dużych liter ma mieć hasło? "))
update_characters_left(uppercase_letters)

special_characters = int(input("Ile znaków specjalnych ma mieć hasło? "))
update_characters_left(special_characters)
 
digits = int(input("Ile cyfr ma mieć hasło? "))
update_characters_left(digits)

if characters_left > 0: 
    print("Nie wykorzystano wszystkich zdeklarowanych znaków. Pozostałe znaki zostaną uzupełnione znakami specjalnymi.")
    special_characters += characters_left

print()
print("Liczba małych liter:", lowercase_letters)
print("Liczba dużych liter:", uppercase_letters)
print("Liczba znaków specjalnych:", special_characters)
print("Liczba cyfr:", digits)

for i in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1 
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -=1
    if digits > 0:
        password.append(random.choice(string.digits))

    random.shuffle(password)
    print("Wygenerowane hasło:", "".join(password))