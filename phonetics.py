#!/usr/bin/python
#Phonetics
default_type = 'c'
def getChar(x, ctype):
    if ctype == 'm':
        return military [x]
    else:
        return civilian [x]

military = {
    'a':'alpha',
    'b':'bravo',
    'c':'charlie',
    'd':'delta',
    'e':'echo',
    'f':'foxtrot',
    'g':'golf',
    'h':'hotel',
    'i':'india',
    'j':'juliet',
    'k':'kilo',
    'l':'lima',
    'm':'mike',
    'n':'november',
    'o':'oscar',
    'p':'papa',
    'q':'quebec',
    'r':'romeo',
    's':'sierra',
    't':'tango',
    'u':'uniform',
    'v':'victor',
    'w':'whisky',
    'x':'x-ray',
    'y':'yankee',
    'z':'zulu'
    }

civilian = {
   'a':'adam',
   'b':'boy',
    'c':'charles',
    'd':'david',
    'e':'edward',
    'f':'frank',
    'g':'george',
    'h':'henry',
    'i':'ida',
    'j':'john',
    'k':'king',
    'l':'lincoln',
    'm':'mary',
    'n':'nora',
    'o':'ocean',
    'p':'paul',
    'q':'queen',
    'r':'robert',
    's':'sam',
    't':'tom',
    'u':'union',
    'v':'victor',
    'w':'william',
    'x':'x-ray',
    'y':'yellow',
    'z':'zebra'
    }



print ('Civilian = c, Military = m')
answer = raw_input ('Type(c/m):')
ri = raw_input ('Word: ')
ri = ri.lower ()
default_type
for ch in ri:
    try:
        phonetic = getChar(ch, answer)
        print ch + " = " + phonetic
    except:
        continue

