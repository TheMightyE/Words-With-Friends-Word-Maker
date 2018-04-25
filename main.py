import sys
from sets import Set
import re
import Word as w

def main():
    letters = sys.argv[1]
    # print(word.s)
    words = getWords(letters)
    # print words
    # print(words)
    scoredWords = []
    for i in words:
        s = w.Word(i, len(i), score(i))
        scoredWords.append(s)
        # print(i)
    # word = w.Word(s, len(s))
    # print removeLetter('hello', 'l')
    # scoredWords = scoredWords.sort()
    newlist = sorted(scoredWords, key=lambda x: x.points, reverse=True)
    for i in newlist:
        print (i.word + ': ' + str(i.points))

def score(word):
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
    score = 0
    for ch in word:
        score = score + letterPoints[ch]
    return score

def getWords(letters):
    filename = 'enable-word-list.txt'

    possibleWords = []
    with open(filename) as inF:
        for line in inF:
            line = replaceNonAlnum(line)
            if len(line) > 1 and len(line) <= len(letters):
                good = False
                tmp = letters
                for c in line:
                    if c in tmp:
                        good = True
                        tmp = removeLetter(tmp, c)
                    else:
                        good = False
                        break
                if good:
                    possibleWords.append(line)
                #     print line

    return possibleWords

def replaceNonAlnum(s):
    p = re.compile(r'[^a-zA-Z0-9:-]+')
    #p = re.compile(r'\W+') # replace whitespace chars
    new = p.sub(' ',s)
    return new.strip()

def removeLetter(s, c):
    indx = s.find(c)
    s2 = ''
    for i in range(len(s)):
        if i != indx:
            s2 = s2 + s[i]
    return s2

main()


#local group = few dozen small
#major galaxy in local group = 2 or 3
