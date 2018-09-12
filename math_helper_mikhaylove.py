''' add(5, 2) ...
'''


import math

def main():
    ''' The main component of Math Helper
        Allows user to select and use five different formulas related to math '''
    #Helper for Math Class (5 Formulas)
    print("Welcome to Egor's Math Helper")
    print()
    print("Here is a list of all of the five formulas which are availiable in Math Helper:")
    while True:
        print("1. Pythagorean Theorem")
        formula = int(input("Please select the formula: "))
        if formula == 1:
            #Formula 1: Pythagorean Theorem
            x = float(input("1st Side Length: "))
            y = float(input("2nd Side Length: "))
            print("The hypotenuse is: {:0.2f}".format(pyth(x, y)))
        else:
            print("That is not an option.")
        
        again = input("Would you like to use another formula? (y/n) ")
        if again == "n" or again == "N":
            print("Thank you for using Egor's Math Helper.")
            return False
            
            
def pyth(x, y):
    ''' Returns the value for the hypotenuse
        using Pythagorean Theorem '''
    answer = math.sqrt(x**2 + y**2)
    return answer

if __name__ == "__main__":
    main()