import random
types_of_characters = {
    "lower": "abcdefghijklmnopqrstuvwxyz",
    "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digits": "0123456789",
    "special": "!@#$%^&*()_+-="
}

length = int(input("Enter the length of the password: "))

password = []

for character_type in types_of_characters:
    password.append(random.choice(types_of_characters[character_type]))

while len(password) < length:
    character_type = random.choice(list(types_of_characters.keys()))
    character = random.choice(types_of_characters[character_type])
    password.append(character)

random.shuffle(password)

password_string = "".join(password)

print("Random password:", password_string)
