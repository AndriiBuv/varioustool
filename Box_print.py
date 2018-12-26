
def boxPrint(symbol, width, heigh):

    print (symbol*width)
    for i in range(heigh - 2):
        print (symbol + (' '*(heigh-2)) + symbol)

    print(symbol*width)


for s, w, h in ((6, 5, 7), ('x',7,7), ('ha', 5, 7)):
    try:
        boxPrint(s,w,h)
    except Exception as err:
        print ("Error %s"% err)
