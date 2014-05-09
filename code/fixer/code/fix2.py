toFix = open('./temp/fixed1').readlines()
fixed = open('./temp/fixed2','w')

i = 0
while i < len(toFix):
    if toFix[i][0:9] == "URIError:":
        i = i + 3
        continue
    fixed.write(toFix[i])
    i = i + 1
fixed.close()

		
