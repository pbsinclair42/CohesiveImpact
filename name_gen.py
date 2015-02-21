def startup_words():
	buzzadj = ['grass-roots', 'synergistic' , 'proactive','adhesive','cohesive','practical','robust','sustainabale','functional','transformative','dynamic']
	buzznouns = ['synergy', 'adhesion','cohesion','impact','globalization']
	computer = ['cache','api','mainframe','firewall','server','cloud','RAM','online']
	company = ['.com','enterprises','ltd','international','incorporated','consolidated']
	x = random.randint(0,3)
	y = random.randint(0,6)
	z = random.randint(0,9)
	output = [ buzzadj[y] + company[x], buzzadj[z] + buzznouns[x], computer[y] + company[x], buzzadj[z] + computer[y] + company[x]]
	return output[x]
