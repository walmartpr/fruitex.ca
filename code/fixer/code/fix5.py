import sys

toFix = open('./temp/fixed4').readlines()
fixed = open('./output/' + sys.argv[1] + '.sex','w')

i = 0
while i < len(toFix):
    first = toFix[i].find('\t')
    second = toFix[i].find('\t',first + 1)
    third = toFix[i].find('\t',second + 1)
    fourth = toFix[i].find('\t',third + 1)
    #print toFix[i][second + 1:second + 6]
    #print toFix[i][third + 1:third + 6]
    #print toFix[i][fourth + 1:fourth + 6]
    #print i
    if toFix[i][second + 1:second + 6] != 'block' and toFix[i][third + 1:third + 6] != 'block' and toFix[i][fourth + 1:fourth + 6] != 'block':
        i = i + 1
        continue
    fixed.write(toFix[i])
    i = i + 1
fixed.close()

		
