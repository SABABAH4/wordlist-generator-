import random
import string
import os

# ==============================
# CONFIGURATION
# ==============================
USE_LETTERS = True
USE_NUMBERS = True
USE_SYMBOLS = True

WORD_LENGTH = 8
WORDS_PER_FILE = 100
NUMBER_OF_FILES = 3
OUTPUT_FOLDER = "output"

# ==============================
# CHARACTER SET
# ==============================
characters = ""

if USE_LETTERS:
    characters += string.ascii_letters

if USE_NUMBERS:
    characters += string.digits

if USE_SYMBOLS:
    characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

if not characters:
    raise ValueError("You must enable at least one character set!")

# ==============================
# SETUP
# ==============================
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def generate_word(length):
    return ''.join(random.choice(characters) for _ in range(length))

# ==============================
# GENERATE FILES
# ==============================
for file_index in range(1, NUMBER_OF_FILES + 1):
    file_path = os.path.join(OUTPUT_FOLDER, f"words_{file_index}.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        for _ in range(WORDS_PER_FILE):
            f.write(generate_word(WORD_LENGTH) + "\n")

print("✅ Wordlists generated successfully!")
