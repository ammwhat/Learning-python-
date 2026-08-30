nato_dict = {
    "A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", 
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet", 
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", 
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", 
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", 
    "Z": "Zulu"
}

Word_to_translate = input("Enter a word:").upper()
letter_list = [nato_dict[letter] for letter in Word_to_translate if letter in nato_dict]
print(" ".join(letter_list))

