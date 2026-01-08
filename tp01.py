import random
import string

letters=string.ascii_letters

c=""
counter=0
while c != "w":
    c=random.choice(letters)
    print(f"la lettre choisie est {c}")
    counter+=1

print(f"Le nombre de tirage effectué est {counter}")