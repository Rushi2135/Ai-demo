"""This is a calculator"""

# ADD function defination

def addition(n1,n2):
	print("The addition is:",n1+n2)

# SUB function defination

def subtract(n1,n2):
	print("The subtraction is: ",n1-n2)

if __name__ == "__main__":
	n1 = int(input("Enter num1"))
	n2 = int(input("Enter num2"))

	#ADD function call below
	addition(n1,n2)
	#SUB function call below
	subtract(n1,n2)
