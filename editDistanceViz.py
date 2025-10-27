# geek for geeks and AI
import nltk
from nltk.corpus import words
import threading
import time
from functools import lru_cache
from png_editDistance import createGIF

nltk.download('words')
english_words = words.words()

print(len(english_words))  
print(english_words[:10])  

#@lru_cache
def editDistRec(s1, s2, m, n):
    global d,c
    if (m,n) in d:
        return d[m,n][0]
        
    if m == 0:
        d[m,n] = n,c

    elif n == 0:
        d[m,n] = m,c

    elif s1[m - 1] == s2[n - 1]:
        d[m,n] = editDistRec(s1, s2, m - 1, n - 1),c
    
    else:
        if ((m,n-1),(m-1,n),(m-1,n-1)) in d:
            d[m,n] = 1 + min(d[m,n-1],d[m-1,n],d[m-1,n-1]), c
        
        else:
            d[m,n] = 1 + min(editDistRec(s1, s2, m, n - 1),
                   editDistRec(s1, s2, m - 1, n),
                   editDistRec(s1, s2, m - 1, n - 1)),c
    
    c+=1
    return d[m,n][0]

d = {}
c=0
def editDistance(s1, s2):
    global d, c
    d={}
    c=0
    return editDistRec(s1, s2, len(s1), len(s2))


editDistance("Word","World")
d_a = [(k,v) for k,v in d.items()]
d_a.sort(key=lambda x:x[1][1])
print(d_a)
createGIF(4,5,"firstI","word_world.gif",d_a)
editDistance("Yell","Hello")
d_a = [(k,v) for k,v in d.items()]
d_a.sort(key=lambda x:x[1][1])
print(d_a)
createGIF(4,5,"secondI","yell_hello.gif",d_a)
editDistance("aabbbcc","abbac")
d_a = [(k,v) for k,v in d.items()]
d_a.sort(key=lambda x:x[1][1])
print(d_a)
createGIF(7,5,"thirdI","aabbcc.gif",d_a)
