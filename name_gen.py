from random import randint

def startup_words():
	buzzadj = ['grass-roots', 'synergistic' , 'proactive','adhesive','cohesive','practical','robust','sustainabale','functional','transformative','dynamic','Social','Crowdsourced']
	buzznouns = ['synergy', 'adhesion','cohesion','impact','globalization','Solutions','Administration','Management','Paradigms']
	computer = ['cache','api','mainframe','firewall','server','cloud','RAM','online', 'Sentiment Analysis','Algorithm']
	company = ['.com','enterprises','ltd','international','incorporated','consolidated', 'global']
	x = randint(0,3)
	y = randint(0,6)
	z = randint(0,5)
	output = [ buzzadj[y] + ' ' + company[x], buzzadj[z] + ' ' +  buzznouns[z], computer[x] + ' ' + company[y], buzzadj[x] + ' ' +  computer[y] + ' ' +  company[z], 'Advanced Virtual Lawnmowers']
	return output[y]

print startup_words()
