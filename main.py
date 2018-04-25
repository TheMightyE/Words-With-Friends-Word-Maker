import sys
from sets import Set
import re
import Word as w

def main():
    letters = sys.argv[1]
    words = getWords(letters)
    scoredWords = []
    for i in words:
        s = w.Word(i, len(i), score(i))
        scoredWords.append(s)

    ''' Sort the words in decending order based on their points '''
    newlist = sorted(scoredWords, key=lambda i: i.points, reverse=True)

    for i in newlist:
        print (i.word + ': ' + str(i.points))

def score(word):
    ''' Define what each letter is worth in the game '''
    letterPoints = {
        'a':1,
        'b':4,
        'c':4,
        'd':2,
        'e':1,
        'f':4,
        'g':3,
        'h':3,
        'i':1,
        'j':10,
        'k':5,
        'l':2,
        'm':4,
        'n':2,
        'o':1,
        'p':4,
        'q':10,
        'r':1,
        's':1,
        't':1,
        'u':2,
        'v':5,
        'w':4,
        'x':8,
        'y':3,
        'z':10
    }
    ''' Calculate the score '''
    score = 0
    for ch in word:
        score = score + letterPoints[ch]
    return score

def getWords(letters):
    ''' Using the list that is used by the game '''
    filename = 'enable-word-list.txt'

    possibleWords = []
    with open(filename) as inF:
        for line in inF:
            ''' Remove characters like the new line character '''
            line = replaceNonAlnum(line)

            '''
            Only check the words that are less than or equal
            to the length of the letters
            '''
            if len(line) <= len(letters):
                good = False
                ''' Copy the original letters string '''
                tmp = letters
                for char in line:
                    if char in tmp:
                        good = True
                        '''
                        Every time a letter from the tmp string is checked,
                        it is removed from the string. This is useful if the
                        letters string has duplicate letters.
                        '''
                        tmp = removeLetter(tmp, char)
                    else:
                        good = False
                        break
                if good:
                    possibleWords.append(line)

    return possibleWords

def replaceNonAlnum(s):
    p = re.compile(r'[^a-zA-Z0-9:-]+')
    #p = re.compile(r'\W+') # replace whitespace chars
    new = p.sub(' ',s)
    return new.strip()

def removeLetter(s, c):
    indxToRemove = s.find(c)
    newStr = ''
    for i in range(len(s)):
        if i != indxToRemove:
            newStr = newStr + s[i]
    return newStr

main()


#local group = few dozen small
#major galaxy in local group = 2 or 3
