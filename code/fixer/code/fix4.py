toFix = open('./temp/fixed35').readlines()
fixed = open('./temp/fixed4','w')

i = 0
while i < len(toFix):
	first = toFix[i].find('\t')
	second = toFix[i].find('\t',first + 1)
	third = toFix[i].find('\t',second + 1)
	fourth = toFix[i].find('\t',third + 1)
	fifth = toFix[i].find('\t',fourth + 1)

	price = toFix[i][first + 1:second]


	if price == '':
		i = i + 1
		continue
	fixed.write(toFix[i])
	i = i + 1
fixed.close()

		
