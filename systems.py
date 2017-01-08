class LineItem(object):
	def __init__(self):
		self.a = 0
		self.v = 0

	def getUpdate(self):
		return (self.a, self.v)
		

class LineItemFactory(object):
	#INTERFACE
	def makeLineItem(self):
		print NotImplementedError("Subclass must implement abstract method")

	def printReport(self):
		print "items Initialized"



class LineItemFactoryImplementation(LineItemFactory):
	def makeLineItem(self):
		item = LineItem()
		item.a = 1
		item.v = 2
		return item



class OrderProcessing(object):
	def run(self, factory):
		newItem = factory.makeLineItem()
		print newItem.getUpdate()

		factory.printReport()


def main():

	factory = LineItemFactoryImplementation()
	orderProcessor = OrderProcessing()
	orderProcessor.run(factory)


if __name__ == "__main__":
	main()
