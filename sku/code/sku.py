import sys

libary		=	open('./code/merge.csv').readlines()


i = 0

while i < len(libary):
	first		=	libary[i].find('","')
	second		=	libary[i].find('","',first + 1)
	third		=	libary[i].find('","',second + 1)
	fourth		=	libary[i].find('","',third + 1)
	fifth		=	libary[i].find('","',fourth + 1)

	sku			=	libary[i][1:first]
	name		=	libary[i][first + 3:second]
	price		=	libary[i][second + 3:third]
	instock 	=	libary[i][third + 3:fourth]
	category 	=	libary[i][fourth + 3:fifth]

	if sku == sys.argv[1]:
		print '"'+ sku + '","' + name + '","' + price + '","' + category + '"'
		print >> sys.stderr, sku + '\t' + name + '\t' + price + '\t' + category
	i = i + 1


