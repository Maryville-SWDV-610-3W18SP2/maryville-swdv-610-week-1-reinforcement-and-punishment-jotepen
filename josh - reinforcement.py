
#test n and m to see if n is a multiple of m
def is_multiple(n, m):
    if m%n == 0:
        #I added the print statement for testing purposes
        print("True")
        return True
    else:
        #I added the print statement for testing purposes
        print("False")
        return False
   
def main():
    #request input from the user for n and m
    n = int(input("Please enter a number: "))
    m = int(input("Please enter another number: "))
    #call the function and pass the inputed variables from the user
    is_multiple(n, m)
    
main()
