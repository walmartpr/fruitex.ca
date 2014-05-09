toFix = open('./temp/fixed2').readlines()
fixed = open('./temp/fixed3','w')

i = 0
while i < len(toFix):
    if toFix[i][1:10] == "undefined":
        i = i + 1
        continue
    fixed.write(toFix[i])
    i = i + 1
fixed.close()

		
