toFix = open('./temp/fixed3').readlines()
fixed = open('./temp/fixed35','w')

i = 0
while i < len(toFix):
	first = toFix[i].find('\t')
	second = toFix[i].find('\t',first + 1)
	third = toFix[i].find('\t',second + 1)
	fourth = toFix[i].find('\t',third + 1)
	fifth = toFix[i].find('\t',fourth + 1)
	sixth = toFix[i].find('\t',fifth + 1)
	seventh = toFix[i].find('\t',sixth + 1)
	eighth = toFix[i].find('\t',seventh + 1)
	nighth = toFix[i].find('\t',eighth + 1)
	tenth = toFix[i].find('\t',nighth + 1)
	eleventh = toFix[i].find('\t',tenth + 1)

	name = toFix[i][:first]
	price = toFix[i][first + 1:second]
	instock = toFix[i][second + 1:third]
	limited = toFix[i][third + 1:fourth]
	outofstock = toFix[i][fourth + 1:fifth]
	image = toFix[i][seventh + 1:eighth]
	discription = toFix[i][eighth + 1:nighth]
	category = toFix[i][nighth + 1:tenth]
	pricelocal = toFix[i][tenth + 1:eleventh]
	pricewas = toFix[i][eleventh + 1:]
	
	if price == "":
		price = pricelocal

	fixed.write(name + '\t' + price  + toFix[i][second: tenth]  + '\t' + pricewas[7:-1] + '\n')
	i = i + 1
fixed.close()

