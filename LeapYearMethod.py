# @author Arash

# determine if a year is a leap year or not. The method signature is as follows:
# static boolean isLeapYear(int year)
# Modify your main program to invoke the method isLeapYear() 
# appropriately so the program functions exactly same as in class exercise 4.  
	
def isLeapYear(year):
	#check leap year
	if (year%4 != 0):
		flag = False
	elif (year%100 != 0):
		flag = True
	elif (year%400 != 0):
		flag = False
	else: 
		flag = True			
	return flag

while (True):
#takes the user input
	print("Please enter a year: (0 to stop) ")
	year = int(input())

	#check if the loop needs to break
	if (year == 0):
		print("Bye.")
		break;
	if (isLeapYear(year)):
		print(year, "is a leap year!");
	else: 
		print(year, "is NOT a leap year!");
