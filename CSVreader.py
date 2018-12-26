
import csv, os.path, pprint

folder = 'path to folder'
file = 'filename.xyz'

exampleFile = open(os.path.join(folder, file))
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

pprint.pprint (exampleData)

newlist = []
for i in exampleData:
    for j in range(len(i[0])):
        if i[0][j] == ';':
            a = i[0].replace(';', '')
    newlist.append(a)



while '' in newlist:
    newlist.remove('')



print (newlist)


