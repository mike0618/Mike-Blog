import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    pass
    # Access key and value

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    pass

# Keyword Method with iterrows()
print({row.student:row.score for i, row in student_data_frame.iterrows()})

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for i, row in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print([nato_dict[letter.upper()] for letter in input('Enter a word: ')])
