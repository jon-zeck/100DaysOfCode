''' DAY 26 - Transform any given string into its NATO ALPHABET Components '''

#### TESTING ZONE ####
# names = ["Alex", "Beth", "Caroline", "Eleanor", "Freddie"]
# arr = [name.upper() for name in names if len(name) > 5]
# print(arr)

# dic = {name:random.randint(0,10) for name in names }
# print(dic)

# passed = {name:score for (name, score) in dic.items() if score > 7}
# print(passed)

import pandas as pd
import os

def find_path(name):
    cwd = os.getcwd()
    for root, _, files in os.walk(cwd):
        if name in files:
            return os.path.join(root, name)
    raise Exception()

try:
    path = find_path("nato_phonetic_alphabet.csv")
except:
    print("Could not find phonetic alphabet")
    exit()

alphabet_df = pd.read_csv(path)

alphabet_dic = {row.letter:row.code for (_, row) in alphabet_df.iterrows()}

name = input("What is your first name? ")
# split_name = name.split() ### WE WILL ASSUME ONLY ONE NAME IS GIVEN
phon_spelling = [alphabet_dic[letter.upper()] for letter in name]

print(phon_spelling)