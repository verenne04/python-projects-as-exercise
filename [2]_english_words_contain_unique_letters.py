# Write a Python program that takes an input string from the user and searches for all
# the English words containing at least once all the unique letters contained in the
# sequence. You are given the English dictionary in a  csv  file to search for the
# correct words. When you found them, display them all, with their definitions.
import csv

FNAME = 'files/dictionary.csv'

def loadDictionary(fname):
    dictionary = {}
    with open(fname, 'r') as fin:
        myreader = csv.reader(fin)
        for row in myreader:
            wordk = row[0].lower()
            if wordk in dictionary.keys():
                dictionary[wordk].append(row[2])
            else:
                dictionary[wordk] = [row[2]]
    return dictionary

def getUniqueLetters(w):
    charset = ''
    for ch in w:
        if not ch in charset:
            charset += ch
    return charset

def findWordsWithCharacters(charset, dict):
    matchingwords = []
    setlen = len(charset)
    for word in dict.keys():
        if len(word) >= setlen:
            allCharAppear = True
            for ch in charset:
                if not ch in word:
                    allCharAppear = False
                    break
            if allCharAppear:
                matchingwords.append(word)
    return matchingwords


# main flow
e_dict = loadDictionary(FNAME)

word = input('Provide a word: ')

wordchs = getUniqueLetters(word)

matchingwords = findWordsWithCharacters(wordchs, e_dict)

# displaying
if matchingwords: 
    for word in matchingwords: 
        print(f'{word} : {" | ".join(e_dict[word])}') 
else: 
    strOut = ", ".join(wordchs) 
    print("No words found including all characters ["  + strOut + "]")

