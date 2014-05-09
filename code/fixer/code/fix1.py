import sys

toFix = open(sys.argv[1]).readlines()
fixed = open('./temp/fixed1','w')

i = 0
while i < len(toFix):
    if toFix[i][0:15] == "ReferenceError:":
        i = i + 3
        continue
    fixed.write(toFix[i])
    i = i + 1
fixed.close()

		
