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
    text = text.upper() #.upper is to convert the text to be all uppercase and it match with the dictionary

    translated_text = [] #The blank set as the storage of the answer that after translated to morse code
    for char in text:
        if char in morse_code_dict:
            translated_text.append(morse_code_dict[char]) #If the character is match and in the dictionary in will append(added) into the list 
        elif char == " ": 
            translated_text.append("/") # If it is blank so it will be / as the symbol 
    return " ".join(translated_text)  #.join is to join each result in the set which in this case is translated_text and joined with " "
    #as the symbol before .join

# Test cases
print(morse_translator("HELLO WORLD"))
print(morse_translator("Python"))
print(morse_translator("Morse Code"))
