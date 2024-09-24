def calculate_area(D1,D2,shape="triangle"):
    if shape == "triangle":
        area = 1/2*D1*D2
        return area
    elif shape == "rectangle":
        area = D1*D2
        return area
    else:
        print("Input is neither triangle nor rectangle")
        area = None
        return area
    
shape= "square"
print("Shape is :",shape)

D1 = 4
D2 = 6
area = calculate_area(4,6,"triangle")
print("Area of triangle is :",area)

D1 = 4
D2 = 4
area = calculate_area(4,4,"rectangle")
print("Area of rectangle is :", area)

area = calculate_area(4,6,"triangle")
print("Area with neither triangle nor rectangle is:",area)


    