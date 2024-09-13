from itertools import combinations, permutations, product
import json

def all_combinations(letters: str):
    all_combinations = []
    letters_list = list(letters)
    
    for length in range(3, len(letters_list) + 1):  # From 3 to the length of the letters
        # Generate all combinations of the given length
        for comb in combinations(letters_list, length):
            # Generate all permutations of the selected combination
            for perm in permutations(comb):
                all_combinations.append(''.join(perm))
    
    return all_combinations
    
def check(words: list):
    res = []
    with open('words.json','r') as file:
        data = json.load(file)
    
    for word in words: 
        if word in data:
            res.append(word)
    return res

letters = []
inp = input("Enter Letters (with no space): ")
for char in inp:
    letters.append(char)
combs = all_combinations(letters)

ans = check(combs)
print(ans)
