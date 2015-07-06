from random import randint

def startup_words():

	buzzadj = ['Grass-roots', 'Synergistic' , 'Proactive','Adhesive','Cohesive','Practical','Robust','Sustainabale','Functional','Transformative','Dynamic','Social','Crowdsourced','Inspirational','Innovative','Strategic','World Class','Active','Holistic','World Wide','Game Changing','Professional','Effective','Maximum Value']
	buzznouns = ['Synergy', 'Adhesion','Cohesion','Impact','Globalization','Solutions','Administration','Management','Paradigms','Social Media','Innovation','Linkativity','Boundarylessness','Collaboration','Networking','Professionalism','Intersubjectivity','Performativity']
	computer = ['Cache','APIs','Mainframes','Firewalls','Servers','Cloud','RAM', 'Sentiment Analysis','Algorithms','Virtual Reality','Multimedia','Data Visualisation','GUI','User Experience','Bootstrapping','Technology','CPUs','Motherboards','Parallels','Semantics','Scripting']
	company = ['.com','Enterprises','Ltd.','International','Incorporated','Consolidated', 'Solutions','Association','Corporation','Foundation','Institute','Society','Applications','Syndicate','Cooperative']
	output = [ buzzadj[randint(0,len (buzzadj) -1)] + ' '+  buzznouns[randint(0,len (buzznouns ) -1)]+' '+ company[randint(0,len (company) -1)], buzzadj[randint(0,len (buzzadj) -1)] + ' ' +  computer[randint(0,len (computer) -1)] + ' ' +  company[randint(0,len (company) -1)], buzzadj[randint(0,len (buzzadj) -1)] + ' ' +  computer[randint(0,len (computer) -1)] ]
	if randint(0,100)==100:
		return 'Advanced Virtual Lawnmowers'
	toReturn = output[randint(0,len (output) -1)] 
	if toReturn[-4:-3]=='.':
		toReturn=toReturn.replace(" ","")
	return toReturn

#print startup_words()
