with open('E:/Python Case study/Case-1/radishsurvey.txt') as oTxtFile:
    oLines = oTxtFile.readlines()
    listRadish = []
    listName = []
    for oLine in oLines:
        oSplitLine = oLine.split('-')
        name_Radish = oSplitLine[-1].strip()
        if name_Radish.count(" ") > 1:
            name_Radish = name_Radish.replace('  ', ' ')
        listRadish.append(name_Radish.lower())

        name_Grocer = ''.join(oSplitLine[:-1])
        listName.append(name_Grocer.lower())

from collections import Counter

print(Counter(listRadish).most_common(1))                        #Most frequent Radish
print(Counter(listRadish).most_common()[-1])                     #Least frequent Radish
print([x for x in Counter(listName).most_common() if x[1]>1])    #Multiple entry of name
oTxtFile.close()



We are learning python here

#{'april cross': 72, 'champion': 76, 'cherry belle': 58, 'snow belle': 63, 'bunny tail': 72, 'sicily giant': 57, 'plum purple': 57, 'red king': 56, 'daikon': 63, 'white icicle': 65, 'french breakfast': 72})
