import sys

toFix = open('./output/' + sys.argv[1] + '.sex').readlines()
fixed = open('./output/' + sys.argv[1] + '-imge.csv','w')

i = 0
while i < len(toFix):
	toFix[i] = toFix[i].replace('"', "inch",100000)
	first = toFix[i].find('\t')
	second = toFix[i].find('\t',first + 1)
	third = toFix[i].find('\t',second + 1)
	fourth = toFix[i].find('\t',third + 1)
	fifth = toFix[i].find('\t',fourth + 1)
	sixth = toFix[i].find('\t',fifth + 1)
	seventh = toFix[i].find('\t',sixth + 1)
	eighth = toFix[i].find('\t',seventh + 1)
	nighth = toFix[i].find('\t',eighth + 1)
	name = toFix[i][:first]
	price = toFix[i][first + 1:second]
	instock = toFix[i][second + 1:third]
	limited = toFix[i][third + 1:fourth]
	image = toFix[i][seventh + 1:eighth]
	discription = toFix[i][eighth + 1:nighth]
	category = toFix[i][nighth + 1:]
	category = category.replace("$", '-',100000)
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
	
	if image[0:2] == "//":
		image = "http:" + image

	price = str(price)
	fname = hex(ord(name[0:1]))[len(hex(ord(name[0:1]))) - 2: len(hex(ord(name[0:1])))].upper()
	namehex = hex(len(name))[len(hex(len(name))) - 2: len(hex(len(name)))].upper()
	lname = hex(ord(name[len(name) - 1: len(name)]))[len(hex(ord(name[len(name) - 1: len(name)]))) - 2: len(hex(ord(name[len(name) - 1: len(name)])))].upper()
	fcategory = hex(ord(category[12:13]))[len(hex(ord(category[12:13]))) - 2: len(hex(ord(category[12:13])))].upper()
	categoryhex = hex(len(category))[len(hex(len(category))) - 2: len(hex(len(category)))].upper()
	lcategory = hex(ord(category[len(category) - 3: len(category) - 2]))[len(hex(ord(category[len(category) - 3: len(category) - 2]))) - 2: len(hex(ord(category[len(category) - 3: len(category) - 2])))].upper()
	fprice = hex(int(price[0:1]))[len(hex(int(price[0:1]))) - 2: len(hex(int(price[0:1])))].upper()
	pricehex = hex(len(price))[len(hex(len(price))) - 2: len(hex(len(price)))].upper()
	sku = fname + namehex + lname + fcategory + categoryhex + lcategory + fprice + pricehex

	if image[len(image) -3: len(image)] != 'jpg' and image[len(image) -3: len(image)] != 'peg':
		fixed.write(sku + '\t' + image[len(image) -3: len(image)] + '\n')
	i = i + 1
fixed.close()

		
