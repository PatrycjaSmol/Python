import sys

no_of_tries = 6
word = "patka"

user_word = []
used_letters = []

def find_indexes (word, letter_in_word):
    indexes = []
    
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)



    return indexes



for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj literę: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery.")
        no_of_tries -=1
        print("Pozostało prób:", no_of_tries)

        if no_of_tries == 0:
            print("Koniec gry!")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter
        
        print("".join(user_word))

        if "".join(user_word) == word:
            print("Brawo! Wygrałeś!")
            sys.exit(0)

        if user_word == int:
            print("Wpisz wybraną literę.")  

    print("Użyte litery:", used_letters)
