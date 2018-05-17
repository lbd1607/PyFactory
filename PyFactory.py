#Laura Davis 1 July 2017

#Lesson and source code from YouTube user Trevor Payne
#This demonstrates how factories are used and created
#with classes and decorators in Python.

#small factory example
BaseClass = type("BaseClass", (object,), {})
C1 = type("C1", (BaseClass,), {"x":1})
C2 = type("C2", (BaseClass,), {"x":30})

def MyFactory(myBool):
	return C1() if myBool else C2()
	
m = MyFactory(True)
v = MyFactory(False)
print m.x, v.x

#decorator classmethod
class MyClass:
	@classmethod
	def printHam(self):
		print "Ham"
		
MyClass.printHam()

#a more robust factory
BaseClass = type("BaseClass" , (object,), {})

@classmethod
def Check1(self, myStr):
	return myStr == "ham"
	
@classmethod
def Check2(self, myStr):
	return myStr == "sandwich"
	
C1 = type("C1", (BaseClass,), {"x":1, "Check":Check1})
C2 = type("C2", (BaseClass,), {"x":30, "Check":Check2})

def MyFactory(myStr):
	for cls in BaseClass.__subclasses__():
		if cls.Check(myStr):
			return cls()
			
m = MyFactory("ham")
v = MyFactory("sandwich")
print m.x, v.x 
