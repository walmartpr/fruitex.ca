import sys

toFix = open('./output/' + sys.argv[1] + '.sex').readlines()
fixed = open('./output/' + sys.argv[1] + '.xml','w')

i = 0
fixed.write("<data>")
while i < len(toFix):
	toFix[i] = toFix[i].replace("&", "&#38;",100000)
	toFix[i] = toFix[i].replace("$", "&#36;",100000)
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

	name = toFix[i][:first]
	price = toFix[i][first + 1:second]
	instock = toFix[i][second + 1:third]
	limited = toFix[i][third + 1:fourth]
	outofstock = toFix[i][fourth + 1:fifth]
	image = toFix[i][seventh + 1:eighth]
	discription = toFix[i][eighth + 1:nighth]
	category = toFix[i][nighth + 1:tenth]
	category = category.replace("&#36;", '-',100000)
	pricewas = toFix[i][tenth + 1:]

	firsts = price.find("<sup>")
	seconds = price.find("</sup>", firsts)
	thirds = price.find("<sup>", seconds)
	fourths = price.find("</sup>", thirds)
	cent1 = price.find("<span>")
	cent2 = price.find("</span>")

	if cent1 != -1:
		price = int(price[cent1 + 6:cent2])
		if price > 9:
			price = "0." + str(price)
		else:
			price = "0.0" + str(price)
	elif thirds != -1:
		right = price[seconds + 6:thirds]
		left = price[thirds + 5:fourths]
		price = right + '.' + left
	else:
		right = price[seconds + 6:]
		price = right

	stock = ''
	if instock == 'block':
		stock = "instock"
	elif limited == 'block':
		stock = "limited"
	elif outofstock == 'block':
		stock = "outofstock"

	if price !="" and pricewas[:-1] != "":
		price = max(float(pricewas[:-1]),float(price))

	if image[0:2] == "//":
		image = "http:" + image
	fixed.write("<item><name>" + name + "</name><price>" + str(price) + "</price><stock>" + stock + "</stock><image>" + image + "</image><discription>" + discription + "</discription><category>" + category + "</category></item>")
	i = i + 1
fixed.write("</data>")
fixed.close()

		
