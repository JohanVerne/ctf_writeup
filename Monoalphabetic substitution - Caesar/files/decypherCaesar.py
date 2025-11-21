with open("ch10.txt", "r") as file:
    text = file.read()


# Emprunté de ce site : https://thepythoncode.com/article/implement-caesar-cipher-in-python
def implement_caesar_cipher(message, key, decrypt=False):
    # Initialize an empty string to store the result.
    result = ""
    # Iterate through each character in the user's input message.
    for character in message:
        # Check if the character is an alphabet letter.
        if character.isalpha():
            # Determine the shift amount based. i.e the amount of times to be shifted e.g 2,3,4....
            shift = key if decrypt else -key
            # Check if the character is a lowercase letter.
            if character.islower():
                # Apply Caesar cipher transformation for lowercase letters.
                result += chr(((ord(character) - ord("a") + shift) % 26) + ord("a"))
            else:
                # Apply Caesar cipher transformation for uppercase letters.
                result += chr(((ord(character) - ord("A") + shift) % 26) + ord("A"))
        else:
            # Preserve non-alphabet characters as they are.
            result += character
    return result  # Return the encrypted or decrypted result.


key = 1
finalText = ""
lines = []
file_lines = text.split("\n")

for file_line in file_lines:
    decrypted_line = ""
    for word in file_line.split():
        decrypted_text = implement_caesar_cipher(word, key, decrypt=True)
        print(f"Key {key}:\n{decrypted_text}\n")
        decrypted_line += decrypted_text + " "
        key += 1
    lines.append(decrypted_line.strip())
    finalText += decrypted_line + "\n"

# Extract first and last letters
first_letters = "".join(line[0] for line in lines if len(line) > 0)
last_letters = "".join(line[-1] for line in lines if len(line) > 0)

print(finalText)
print(lines)
print(f"First letters: {first_letters}")
print(f"Last letters: {last_letters}")
print(f"Concatenation: {first_letters + last_letters}")
