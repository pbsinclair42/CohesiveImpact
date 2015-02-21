from random import randint

def startup_words():

	buzzadj = ['Grass-roots', 'Synergistic' , 'Proactive','Adhesive','Cohesive','Practical','Robust','Sustainabale','Functional','Transformative','Dynamic','Social','Crowdsourced']
	buzznouns = ['Synergy', 'Adhesion','Cohesion','Impact','Globalization','Solutions','Administration','Management','Paradigms']
	computer = ['Cache','API','Mainframe','Firewall','Server','Cloud','RAM','Online', 'Sentiment Analysis','Algorithm']
	company = ['.com','Enterprises','Ltd.','International','Incorporated','Consolidated', 'Global']
	output = [ buzzadj[randint(0,len (buzzadj) -1)] + ' ' + company[randint(0,len (company) -1)], buzzadj[randint(0,len (buzzadj) -1)] + ' ' +  buzznouns[randint(0,len (buzznouns ) -1)], computer[randint(0,len (computer) -1)] + ' ' + company[randint(0,len (company) -1)], buzzadj[randint(0,len (buzzadj) -1)] + ' ' +  computer[randint(0,len (computer) -1)] + ' ' +  company[randint(0,len (company) -1)]]
	return output[randint(0,len (output) -1)] if randint(0,100) else 'Advanced Virtual Lawnmowers'


print startup_words()