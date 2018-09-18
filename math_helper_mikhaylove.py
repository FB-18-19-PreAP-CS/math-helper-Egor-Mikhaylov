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
        print("2. Slope")
        print("3. Inverse Sine")
        formula = int(input("Please select the formula: "))
        if formula == 1:
            #Formula 1: Pythagorean Theorem
            x = float(input("1st Side Length: "))
            y = float(input("2nd Side Length: "))
            print("The hypotenuse is: {}".format(pyth(x, y)))
        elif formula == 2:
            #Formula 2: Slope
            x1 = float(input("X value for the first coordinate: "))
            y1 = float(input("Y value for the first coordinate: "))
            x2 = float(input("X value for the second coordinate: "))
            y2 = float(input("Y value for the second coordinate: "))
            print("The slope is: {}".format(slope(x1, y1, x2, y2)))
        elif formula == 3:
            #Formula 3: Inverse Sine
            opposite = float(input("Value for the opposite side: "))
            hypotenuse = float(input("Value for the hypothenuse: "))
            print(f"The angle is: {inverse_sine(opposite, hypotenuse)}")
        else:
            print("That is not an option.")
        
        again = input("Would you like to use another formula? (y/n) ")
        print()
        if again == "n" or again == "N":
            print("Thank you for using Egor's Math Helper.")
            return False
            
            
def pyth(x, y):
    ''' Returns the value for the hypotenuse
        using Pythagorean Theorem
        
        >>> pyth(5, 7)
        8.6
        
        >>> pyth(34, 45)
        56.4
        
        >>> pyth(9, 1)
        9.06
        
        The inputs should never be 0.
        >>> pyth(6, 0)
        Traceback (most recent call last):
            ...
        ValueError: None of the sides should be 0
        
        The formula can't have any negative inputs.
        >>> pyth(-4, -3)
        Traceback (most recent call last):
            ...
        ValueError: All inputs for pythagorean theorum must be positive.
        '''
    if x == 0 or y == 0:
        raise ValueError("None of the sides should be 0")
    if x < 0 or y < 0:
        raise ValueError("All inputs for pythagorean theorum must be positive.")
    answer = math.sqrt(x**2 + y**2)
    return round(answer, 2)

def slope(x1, y1, x2, y2):
    ''' Returns the slope for two pairs of
    coordinates.
    
        >>> slope(9, 7, 8, 3)
        4.0
        
        >>> slope(-4, -1, 1, -98)
        -19.4
        
        >>> slope(5, 6, 9, 6)
        0.0
        
        >>> slope(2, 9, 2, 17)
        'undefined'
        
        >>> slope(3, 3, 3, 3)
        'no slope'
    '''
    if x1 == x2 == y1 == y2:
        answer = "no slope"
        return answer
    elif x1 != x2:
        answer = (y2-y1)/(x2-x1)
        return round(answer, 2)
    else:
        answer = "undefined"
        return answer
    
def inverse_sine(opposite, hypotenuse):
    answer = (math.asin(opposite/hypotenuse))*180/math.pi
    return round(answer, 2)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #main()