def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

#Convert the text to uppercase to have a applicable for every case sensitivity
    text = text.upper()

    translated_text = []
    for char in text:
        if char in morse_code_dict:
            translated_text.append(morse_code_dict[char])
        elif char == " ":
            translated_text.append("/")
    return " ".join(translated_text) 

# Test cases
print(morse_translator("HELLO WORLD"))
print(morse_translator("Python"))
print(morse_translator("Morse Code"))
