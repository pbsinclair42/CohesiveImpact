from random import randint

def wordGenerator():
	return (randomConsonant(0)+randomVowel()+randomConsonant(1)+(randomVowel()+randomConsonant(1) if (randint(0,1)==0) else "")+randomVowel()+randomConsonant(2)).capitalize()
	
	
def randomVowel():
	vowels=[("a",10),("e",15),("i",10),("o",10),("u",5),("ie",5),("oo",5),("ou",3),("ee",3),("ai",3),("ou",3),("ea",3),("oa",1),("oi",1),("ia",1),("io",1)]
	totalSum=0;
	for a in vowels:
		totalSum+=a[1]
	x=randint(0,totalSum)
	for a in vowels:
		x-=a[1]
		if (x<=0):
			return a[0]

def randomConsonant(position):
	consonants=[("b",6,True,True,True),("c",4,True,True,False),("d",6,True,True,True),("f",4,True,True,False),("g",4,True,True,False),("h",2,True,False,False),("j",2,True,False,False),("k",2,True,False,False),("ck",5,False,True,True),("l",6,True,True,True),("m",6,True,True,True),("n",6,True,True,True),("p",10,True,True,True),("qu",1,True,True,False),("r",10,True,True,True),("s",10,True,True,True),("t",10,True,True,True),("v",3,True,True,False),("w",6,True,True,True),("x",4,False,True,True),("z",2,True,True,True),("bl",1,True,True,False),("br",2,True,True,False),("ch",3,True,True,True),("cl",1,True,True,False),("cr",1,True,True,False),("dr",1,True,False,False),("fl",1,True,False,False),("fr",2,True,False,False),("gr",1,True,True,False),("ph",3,True,True,True),("pl",2,True,True,False),("pr",2,True,True,False),("sc",1,True,False,False),("sh",5,True,True,True),("sk",2,True,True,True),("sl",2,True,True,False),("sn",1,True,True,False),("st",5,True,True,True),("str",3,True,True,False),("sw",2,True,True,False),("th",5,True,True,True),("tr",3,True,True,False),("tw",1,True,False,False),("wh",3,True,False,False),("ng",5,False,False,True)]
	totalSum=0;
	for a in consonants:
		totalSum+=a[1]
	x=randint(0,totalSum)
	toReturn=""
	while True:
		for a in consonants:
			x-=a[1]
			if (x<=0):
				if (a[position+2]):
					return a[0]

#print wordGenerator()