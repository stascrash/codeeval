# import untangle
import xmltodict

def walkDict( aDict, visitor, path=() ):
    for  k in aDict:
        if k == 'attrs':
            visitor( path, aDict[k] )
        elif type(aDict[k]) != dict:
            pass
        else:
            walkDict( aDict[k], visitor, path+(k,) )

def printMe( path, element ):
    print path, element

def filterFor( path, element ):
    if element['id'] == '4130-2-2':
        print path, element

Q
inputXml = r"C:\Users\stanislav.poritskiy\Desktop\Layout 1.xml"
inputDict = None
with open(inputXml) as fd:
	inputDict = xmltodict.parse(fd.read())
fd.close()

for k, v in inputDict.items():
	print k, v
#walkDict(inputDict, filterFor)

# inputObj = untangle.parse(inputXml)

# print (inputObj.c2layout.layers.layer)

# intputProps = ([attr for attr in dir(inputObj) if not attr.startswith('__')])

# for x in intputProps:
# 	print x