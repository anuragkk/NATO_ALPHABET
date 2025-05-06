import pandas

# Read the NATO phonetic alphabet data
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the DataFrame
new_dict = {row['letter']: row['code'] for index, row in data.iterrows()}

# Get user input
name = input("Enter a name:\n ")

# Convert each letter to uppercase and get the phonetic word
phonetic_word = {letter.upper(): new_dict[letter.upper()] if letter.upper() in new_dict else letter for letter in name}

# Print the phonetic word
print(phonetic_word)
