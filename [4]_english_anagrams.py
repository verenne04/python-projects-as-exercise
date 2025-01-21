# Write a Python program that asks the user to input a word in the English 
# language and computes and displays all proper words that are anagrams of 
# the input, also displaying the total number. File “dictionary.txt” (in the 
# resource area on WeBeep) contains the list of all proper words.

FNAME = 'dictionary.txt'

def anagrams(word):
    size = len(word)
    if size == 1:
        return word
    
    result = []

    for i in range(0, size):
        current_letter = word[i]
        res = word[:i] + word[i+1:]
        for anagram in anagrams(res):
            result.append(current_letter+anagram)
    return result

wordin = input()

anags = anagrams(wordin)

result = []
with open(FNAME, 'r') as dic:
    dictionary = dic.readlines()
    counter = 0
    for word in anags:
        if (word+'\n') in dictionary:
            result.append(word)
            counter += 1

print(str(result) + '\n' + f'{counter}')
