import random
import string

# List of all uppercase and lowercase letters
letters = string.ascii_letters

# Initialize variables
selected_letter = ""
draw_count = 0

# Keep drawing letters until 'w' is found
while selected_letter != "w":
    selected_letter = random.choice(letters)
    draw_count += 1
    print(f"La lettre choisie est : {selected_letter}")

# Display total number of draws
print(f"Le nombre de tirages effectués est : {draw_count}")
