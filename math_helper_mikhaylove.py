import math

def main():
    ''' The main component of Math Helper
        Allows user to select and use five different formulas related to math '''
    #Helper for Math Class (5 Formulas)
    print("Welcome to Egor's Math Helper")
    print()
    print("Here is a list of all of the five formulas which are availiable in Math Helper:")
    while True:
        try:
            print("1. Pythagorean Theorem")
            print("2. Slope")
            print("3. Inverse Sine")
            print("4. Midpoint")
            print("5. Distance")
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
            elif formula == 4:
                #Formula 4: Midpoint
                x1 = float(input("X value for the first coordinate: "))
                y1 = float(input("Y value for the first coordinate: "))
                x2 = float(input("X value for the second coordinate: "))
                y2 = float(input("Y value for the second coordinate: "))
                print(f"The midpoint is: {midpoint(x1, y1, x2, y2)}.")
            elif formula == 5:
                #Formula 5: Distance
                x1 = float(input("X value for the first coordinate: "))
                y1 = float(input("Y value for the first coordinate: "))
                x2 = float(input("X value for the second coordinate: "))
                y2 = float(input("Y value for the second coordinate: "))
                print(f"The distance is: {distance(x1, y1, x2, y2)}")
            else:
                print("That is not an option.")
            
            again = input("Would you like to use another formula? (y/n) ")
            print()
            if again == "n" or again == "N":
                print("Thank you for using Egor's Math Helper.")
                return False
            
        except ValueError as e:
            if 'could not convert string to float:' in str(e) or 'invalid literal for int() with base 10' in str(e):
                print('invalid input')
            else:
                print('Error: ' +str(e))
    
        except Exception:
            print("Invalid input")
        
            
            
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
    ''' Returns the angle measurement when given two
        inputs for the sides of a triangle.
        
        >>> inverse_sine(57, 100)
        34.75
        
        >>> inverse_sine(23, 199)
        6.64
        
        The hypotenuse can't be less than the other side.
        >>> inverse_sine(5, 3)
        Traceback (most recent call last):
            ...
        ValueError: The hypotenuse can't ever be less than the opposite side.
        
        None of the inputs should be 0
        >>> inverse_sine(0, 9)
        Traceback (most recent call last):
            ...
        ValueError: None of the sides should be 0.
        
        None of the inputs can be negative.
        >>> inverse_sine(-5, -9)
        Traceback (most recent call last):
            ...
        ValueError: There should be no negative sides.
    '''
    if hypotenuse < 0 or opposite < 0:
        raise ValueError("There should be no negative sides.")
    elif hypotenuse < opposite:
        raise ValueError("The hypotenuse can't ever be less than the opposite side.")
    elif hypotenuse == 0 or opposite == 0:
        raise ValueError("None of the sides should be 0.")
    answer = (math.asin(opposite/hypotenuse))*180/math.pi
    return round(answer, 2)

def midpoint(x1, y1, x2, y2):
    ''' Returns the coordinates of the midpoint of two given coordinates
    
    >>> midpoint(5, 8, 2, 9)
    (3.5, 8.5)
    
    >>> midpoint(23, 8, 2, 59)
    (12.5, 33.5)
    
    >>> midpoint(8, 1, 5, 3)
    (6.5, 2.0)
    
    >>> midpoint(-5, -7, 6, -9)
    (0.5, -8.0)

    The coordinates shouldn't be the same.
    >>> midpoint(6, 3, 6, 3)
    Traceback (most recent call last):
        ...
    ValueError: The coordinates are in the same place.
    '''
    if x1 == x2 and y1 == y2:
        raise ValueError("The coordinates are in the same place.")
    x = (x1+x2)/2
    y = (y1+y2)/2
    return (round(x, 2), round(y, 2))

def distance(x1, y1, x2, y2):
    ''' Returns the distance of two given coordinates

    >>> distance(8, 9, 8, 10)
    1.0
    
    >>> distance(-2, 3, 9, 4)
    11.05
    
    >>> distance(-73, 3, -4, 91)
    111.83
    
    >>> distance(0, -6, 0, -19)
    13.0

    >>> distance(5, 9, 5, 9)
    Traceback (most recent call last):
        ...
    ValueError: The coordinates are in the same place.
    '''
    if x1 == x2 and y1 == y2:
        raise ValueError("The coordinates are in the same place.")
    answer = math.sqrt((x2-x1)**2 + (y2 -y1)**2)
    return round(answer, 2)
    
if __name__ == "__main__":
    main()
 