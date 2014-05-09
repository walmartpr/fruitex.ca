import sys

toFix	=	open(sys.argv[1]).readlines()
lost	=	open(sys.argv[1] + '.lost','w')
none	=	open(sys.argv[1] + '.none','w')
zero	=	open(sys.argv[1] + '.zero','w')
fixed	=	open(sys.argv[1] + '.csv','w')
img	=	open(sys.argv[1] + '.image','w')

i = 0
j = 1
while i < len(toFix):

	first		=	toFix[i].find('","')
	second		=	toFix[i].find('","',first + 1)
	third		=	toFix[i].find('","',second + 1)
	fourth		=	toFix[i].find('","',third + 1)
	fifth		=	toFix[i].find('","',fourth + 1)
	sixth		=	toFix[i].find('","',fifth + 1)
	seventh		=	toFix[i].find('","',sixth + 1)
	eighth		=	toFix[i].find('","',seventh + 1)
	nighth		=	toFix[i].find('","',eighth + 1)
	tenth		=	toFix[i].find('","',nighth + 1)
	eleventh	=	toFix[i].find('","',tenth + 1)
	twelfth		=	toFix[i].find('","',eleventh + 1)
	thirteenth	=	toFix[i].find('","',twelfth + 1)

	url			=	toFix[i][1:first]
	instock		=	toFix[i][first + 3:second]
	limited		=	toFix[i][second + 3:third]
	outofstock 	=	toFix[i][third + 3:fourth]
	name 		=	toFix[i][fourth + 3:fifth]
	category 	=	toFix[i][fifth + 3:sixth]
	discription =	toFix[i][sixth + 3:seventh]
	image 		=	toFix[i][seventh + 3:eighth]
	price 		=	toFix[i][eighth + 3:nighth]
	localprice1	=	toFix[i][nighth + 3:tenth]
	localprice2	=	toFix[i][tenth + 3:eleventh]
	localprice3	=	toFix[i][eleventh + 3:twelfth]
	pricewas1	=	toFix[i][twelfth + 3:thirteenth]
	pricewas2	=	toFix[i][thirteenth + 3:]

	#replace "
	url			= url.replace('"', "inch",100000)
	instock		= instock.replace('"', "inch",100000)
	limited		= limited.replace('"', "inch",100000)
	outofstock 	= outofstock.replace('"', "inch",100000)
	name 		= name.replace('"', "inch",100000)
	category 	= category.replace('"', "inch",100000)
	discription = discription.replace('"', "inch",100000)
	image 		= image.replace('"', "inch",100000)
	price 		= price.replace('"', "inch",100000)
	localprice1 = localprice1.replace('"', "inch",100000)
	localprice2 = localprice2.replace('"', "inch",100000)
	localprice3 = localprice3.replace('"', "inch",100000)
	pricewas1 	= pricewas1.replace('"', "inch",100000)
	pricewas2 	= pricewas2.replace('"', "inch",100000)

	print url	

	#filter
	if url[0:4] != "http":
		i = i + 1
		continue
	if instock == "none" and limited == "none" and outofstock == "none":
		none.write(url + '\n')
		i = i + 1
		continue
	if instock == "undefined" and limited == "undefined" and outofstock == "undefined":
		lost.write(url + '\n')
		i = i + 1
		continue

	#exclude undefined price
	if price == "undefined":
		price = "";
	if localprice1 == "undefined":
		localprice1 = "";
	if localprice2 == "undefined":
		localprice2 = "";
	if localprice3 == "undefined":
		localprice3 = "";
	if pricewas1 == "undefined":
		pricewas1 = "";
	if pricewas2 == "undefined":
		pricewas2 = "";

	#price normalize
	firstprice = price.find("<sup>")
	secondprice = price.find("</sup>", firstprice)
	thirdprice = price.find("<sup>", secondprice)
	fourthprice = price.find("</sup>", thirdprice)
	cent1price = price.find("<span>")
	cent2price = price.find("</span>")
	if cent1price != -1:
		price = int(price[cent1price + 6:cent2price])
		if price > 9:
			price = "0." + str(price)
		else:
			price = "0.0" + str(price)
	elif thirdprice != -1:
		rightprice = price[secondprice + 6:thirdprice]
		leftprice = price[thirdprice + 5:fourthprice]
		price = rightprice + '.' + leftprice
	else:
		rightprice = price[secondprice + 6:]
		price = rightprice
		
	#localprice1 normalize
	if localprice1 != "":
		if localprice1[0] != "1" and localprice1[0] != "2" and localprice1[0] != "3" and localprice1[0] != "4" and localprice1[0] != "5" and localprice1[0] != "6" and localprice1[0] != "7" and localprice1[0] != "8" and localprice1[0] != "9" and localprice1[0] != "0":
			localprice1 = localprice1[1:]
		elif localprice1[-1] != "1" and localprice1[-1] != "2" and localprice1[-1] != "3" and localprice1[-1] != "4" and localprice1[-1] != "5" and localprice1[-1] != "6" and localprice1[-1] != "7" and localprice1[-1] != "8" and localprice1[-1] != "9" and localprice1[-1] != "0": 
			localprice1 = localprice1[:-2]
			if int(localprice1) > 9:
				localprice1 = "0." + localprice1
			else:
				localprice1 = "0.0" + localprice1

	#localprice2 normalize
	firstlocalprice2 = localprice2.find("<sup>")
	secondlocalprice2 = localprice2.find("</sup>", firstlocalprice2)
	thirdlocalprice2 = localprice2.find("<sup>", secondlocalprice2)
	fourthlocalprice2 = localprice2.find("</sup>", thirdlocalprice2)
	cent1localprice2 = localprice2.find("<span>")
	cent2localprice2 = localprice2.find("</span>")
	if cent1localprice2 != -1:
		localprice2 = int(localprice2[cent1localprice2 + 6:cent2localprice2])
		if localprice2 > 9:
			localprice2 = "0." + str(localprice2)
		else:
			localprice2 = "0.0" + str(localprice2)
	elif thirdlocalprice2 != -1:
		rightlocalprice2 = localprice2[secondlocalprice2 + 6:thirdlocalprice2]
		leftlocalprice2 = localprice2[thirdlocalprice2 + 5:fourthlocalprice2]
		localprice2 = rightlocalprice2 + '.' + leftlocalprice2
	else:
		rightlocalprice2 = localprice2[secondlocalprice2 + 6:]
		localprice2 = rightlocalprice2
	
	#localprice3 normalize
	firstlocalprice3 = localprice3.find("<sup>")
	secondlocalprice3 = localprice3.find("</sup>", firstlocalprice3)
	thirdlocalprice3 = localprice3.find("<sup>", secondlocalprice3)
	fourthlocalprice3 = localprice3.find("</sup>", thirdlocalprice3)
	cent1localprice3 = localprice3.find("<span>")
	cent2localprice3 = localprice3.find("</span>")
	if cent1localprice3 != -1:
		localprice3 = int(localprice3[cent1localprice3 + 6:cent2localprice3])
		if localprice3 > 9:
			localprice3 = "0." + str(localprice3)
		else:
			localprice3 = "0.0" + str(localprice3)
	elif thirdlocalprice3 != -1:
		rightlocalprice3 = localprice3[secondlocalprice3 + 6:thirdlocalprice3]
		leftlocalprice3 = localprice3[thirdlocalprice3 + 5:fourthlocalprice3]
		localprice3 = rightlocalprice3 + '.' + leftlocalprice3
	else:
		rightlocalprice3 = localprice3[secondlocalprice3 + 6:]
		localprice3 = rightlocalprice3
	
	#pricewas1 normalize
	if pricewas1 != "":
		if pricewas1[-1] != "1" and pricewas1[-1] != "2" and pricewas1[-1] != "3" and pricewas1[-1] != "4" and pricewas1[-1] != "5" and pricewas1[-1] != "6" and pricewas1[-1] != "7" and pricewas1[-1] != "8" and pricewas1[-1] != "9" and pricewas1[-1] != "0": 
			pricewas1 = pricewas1[pricewas1.rfind(" ") + 1:pricewas1.rfind(" ") + 3]
			if pricewas1[-1] != "1" and pricewas1[-1] != "2" and pricewas1[-1] != "3" and pricewas1[-1] != "4" and pricewas1[-1] != "5" and pricewas1[-1] != "6" and pricewas1[-1] != "7" and pricewas1[-1] != "8" and pricewas1[-1] != "9" and pricewas1[-1] != "0":
				pricewas1 = "0.0" + pricewas1[0:1]
			else:
				pricewas1 = "0." + pricewas1
		elif pricewas1.find('$') != -1:
			pricewas1 = pricewas1[pricewas1.find('$') + 1:]

	#pricewas2 normalize
	firstpricewas2 = pricewas2.find("<sup>")
	secondpricewas2 = pricewas2.find("</sup>", firstpricewas2)
	thirdpricewas2 = pricewas2.find("<sup>", secondpricewas2)
	fourthpricewas2 = pricewas2.find("</sup>", thirdpricewas2)
	cent1pricewas2 = pricewas2.find("<span>")
	cent2pricewas2 = pricewas2.find("</span>")
	strikethrough = pricewas2.find("</strikethrough>")
	if cent1pricewas2 != -1:
		pricewas2 = int(pricewas2[cent1pricewas2 + 6:cent2pricewas2])
		if pricewas2 > 9:
			pricewas2 = "0." + str(pricewas2)
		else:
			pricewas2 = "0.0" + str(pricewas2)
	elif thirdpricewas2 != -1:
		rightpricewas2 = pricewas2[secondpricewas2 + 6:thirdpricewas2]
		leftpricewas2 = pricewas2[thirdpricewas2 + 5:fourthpricewas2]
		pricewas2 = rightpricewas2 + '.' + leftpricewas2
	else:
		rightpricewas2 = pricewas2[secondpricewas2 + 6:strikethrough]
		pricewas2 = rightpricewas2
	
	#get the max price
	if price == "":
		price = 0;
	if localprice1 == "":
		localprice1 = 0;
	if localprice2 == "":
		localprice2 = 0;
	if localprice3 == "":
		localprice3 = 0;
	if pricewas1 == "":
		pricewas1 = 0;
	if pricewas2 == "":
		pricewas2 = 0;
		
	if price == 0 and localprice1 == 0 and localprice2 == 0 and localprice3 == 0 and pricewas1 == 0 and pricewas2 == 0:
		zero.write(url + '\n');
		i = i + 1
		continue
	else:
		price = float(price)
		localprice1 = float(localprice1)
		localprice2 = float(localprice2)
		localprice3 = float(localprice3)
		pricewas1 = float(pricewas1)
		pricewas2 = float(pricewas2)
		price = str(max(price,localprice1,localprice2,localprice3,pricewas1,pricewas2))
	
	#deal with stock
	store = ""
	if instock == "block":
		store = "instock"
	elif limited == "block":
		store = "limited"
	elif outofstock == "block":
		store = "outofstock"

	#deal with image
	if image[0:2] == "//":
		image = "http:" + image

	price = str(price)
	category = category[14:]

	fname = hex(ord(name[0:1]))[len(hex(ord(name[0:1]))) - 2: len(hex(ord(name[0:1])))].upper()
	namehex = hex(len(name))[len(hex(len(name))) - 2: len(hex(len(name)))].upper()
	lname = hex(ord(name[len(name) - 1: len(name)]))[len(hex(ord(name[len(name) - 1: len(name)]))) - 2: len(hex(ord(name[len(name) - 1: len(name)])))].upper()
	fcategory = hex(ord(category[12:13]))[len(hex(ord(category[12:13]))) - 2: len(hex(ord(category[12:13])))].upper()
	categoryhex = hex(len(category))[len(hex(len(category))) - 2: len(hex(len(category)))].upper()
	lcategory = hex(ord(category[len(category) - 3: len(category) - 2]))[len(hex(ord(category[len(category) - 3: len(category) - 2]))) - 2: len(hex(ord(category[len(category) - 3: len(category) - 2])))].upper()
	sku = fname + namehex + lname + fcategory + categoryhex + lcategory +  format(j,"04x")

	fixed.write('"' + sku + '","' + name + '","' + price + '","' + store + '","' + category + '","' + discription + '","' + image + '","' + url + '"\n' )
	img.write(sku + '\t' + image + '\n')
	i = i + 1
	j = j + 1

img.close()
lost.close()
none.close()
zero.close()
fixed.close()
		
