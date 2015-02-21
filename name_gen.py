def startup_words():
	buzzadj = ['grass-roots', 'synergistic' , 'proactive','adhesive','cohesive','practical','robust','sustainabale','functional','transformative','dynamic']
	buzznouns = ['synergy', 'adhesion','cohesion','impact','globalization']
	computer = ['cache','api','mainframe','firewall','server','cloud','RAM','online']
	company = ['.com','enterprises','ltd','international','incorporated','consolidated']
	x = random.randint(0,5)
	return buzzadj[x] + ' ' + buzznouns[x] + ' ' + company[x]