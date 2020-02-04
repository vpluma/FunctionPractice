# Global Variables
flavorPrice = 1.25

def askCustomer():
	#global flavorPrice
	flavorPrice = 2.50
	name = input("What is your name? ")
	age = int(input("How old are you? "))
	flavors = []
	numFlavors = int(input("How many flavors do you want? "))
	for n in range(numFlavors):
		f = input(f"Flavor {n+1} name: ")
		flavors.append(f)
	return name, age, flavors, numFlavors

def printCourses(name, flavors):
	print (f"Hi {name}, you want the following flavors:")
	print("Flavor List: ", end = " ")
	for eachFlavor in flavors:
		print(eachFlavor, end = ", ")
	
def main():
	name, age, flavors, numFlavors = askCustomer()
	printCourses(name, flavors)

main()