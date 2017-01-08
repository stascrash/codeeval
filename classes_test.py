class MainFuncs(object):
    def __init__(self, m_name):
        self.myName = m_name
        self.mainFuncsVar = "This Is Main Functions Class"

    def showText(self):
        print (self.mainFuncsVar)

    def funcToMake(self, giveMe):
        print "GiveMe it: %s" % giveMe

    def funcOver(self):
        print "This is from MAINCLASS"


class SecondFuncs(MainFuncs):
    def printMe(self):
        print "Just printing from SecondFuncs"

    def showName(self):
        print self.myName

    def callFromOther(self):
        self.funcToMake("SPARTA")

    def funcOver(self):
        print "This is new value override"


class SomethingElse(object):
    pass


# aa = MainFuncs(" STASOK ")

# xx = SecondFuncs("Stas")
# # xx.showText()
# # xx.printMe()
# # xx.showName()

# # xx.callFromOther()
# print aa.myName
# print xx.myName

# #aa.funcOver()
# #xx.funcOver()
def sayHi(inner):
    """

    :rtype : Function
    """

    def outHi():
        print ('Just saying hi instead')

    return outHi


def decorator(inner):
    def inner_decorator():
        print('before')
        inner()
        print('after')

    return inner_decorator


@sayHi
def decorated():
    print('now')





decorated()
