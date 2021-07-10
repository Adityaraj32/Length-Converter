print("\t\t\tWelcome to the length converter")

def converter():
    print("\nYou want to convert from")
    print("\tMillimeter(mm)\n\tCentimeter(cm)\n\tDecimeter(dm)\n\tMeter(m)\n\tdecameter(dem)\n\tHectameter(hm)\n\tKilometer(km)")
    from_conver = input("Enter from which you wanna to convert: ")
        
    print("\nYou want to convert to")
    print("\tMillimeter(mm)\n\tCentimeter(cm)\n\tDecimeter(dm)\n\tMeter(m)\n\tdecameter(dem)\n\tHectameter(hm)\n\tKilometer(km)")
    to_conver = input("Enter to which you wanna to convert: ")

    num = int(input(f"\nEnter the number of {from_conver}: "))

    # this will return the same number
    if from_conver == to_conver:
        print(f"{num} {from_conver}")

    # this will convert the number if from_conver is kilometer
    elif from_conver == "Kilometer" or from_conver == "kilometer" or from_conver == "km":
        if to_conver == "Hectameter" or to_conver == "hectameter" or to_conver == "hm":
                print(f"The result is {num*10}")  
        elif to_conver == "Decameter" or to_conver == "decameter" or to_conver == "Dem":
                print(f"The result is {num*100}")
        elif to_conver == "Meter" or to_conver == "meter" or to_conver == "m":
                print(f"The result is {num*1000}")
        elif to_conver == "Decimeter" or to_conver == "decimeter" or to_conver == "dm":
            print(f"The result is {num*10000}")
        elif to_conver == "Centimeter" or to_conver == "centimeter" or to_conver == "cm":
            print(f"The result is {num*100000}")
        elif to_conver == "Milimeter" or to_conver == "milimeter" or to_conver == "mm":
            print(f"The result is {num*1000000}")
    
    
    # this will convert the number if from_conver is Hectameter
    elif from_conver == "Hectameter" or from_conver == "hectameter" or from_conver == "hm":
        if to_conver == "Kilometer" or to_conver == "kilometer" or to_conver == "km":
            print(f"The result is {num/10}")
        elif to_conver == "Decameter" or to_conver == "decameter" or to_conver == "Dem":
                print(f"The result is {num*10}")
        elif to_conver == "Meter" or to_conver == "meter" or to_conver == "m":
                print(f"The result is {num*100}")
        elif to_conver == "Decimeter" or to_conver == "decimeter" or to_conver == "dm":
            print(f"The result is {num*1000}")
        elif to_conver == "Centimeter" or to_conver == "centimeter" or to_conver == "cm":
            print(f"The result is {num*10000}")
        elif to_conver == "Milimeter" or to_conver == "milimeter" or to_conver == "mm":
            print(f"The result is {num*100000}")
    
    
    # this will convert the number if from_conver is Decameter
    elif from_conver == "Decameter" or from_conver == "decameter" or from_conver == "dm":
        if to_conver == "Kilometer" or to_conver == "kilometer" or to_conver == "km":
            print(f"The result is {num/100}")
        elif to_conver == "Hectameter" or to_conver == "hectameter" or to_conver == "hm":
                print(f"The result is {num/10}")  
        elif to_conver == "Meter" or to_conver == "meter" or to_conver == "m":
                print(f"The result is {num*10}")
        elif to_conver == "Decimeter" or to_conver == "decimeter" or to_conver == "dm":
            print(f"The result is {num*100}")
        elif to_conver == "Centimeter" or to_conver == "centimeter" or to_conver == "cm":
            print(f"The result is {num*1000}")
        elif to_conver == "Milimeter" or to_conver == "milimeter" or to_conver == "mm":
            print(f"The result is {num*10000}")

    # this will convert the number if from_conver is Meter
    elif from_conver == "Meter" or from_conver == "meter" or from_conver == "m":
        if to_conver == "Kilometer" or to_conver == "kilometer" or to_conver == "km":
            print(f"The result is {num / 1000} km")
        elif to_conver == "Hectameter" or to_conver == "hectameter" or to_conver == "hm":
            print(f"The result is {num/100}")
        elif to_conver == "Decameter" or to_conver == "decameter" or to_conver == "dem":
            print(f"The result is {num/10}")
        elif to_conver == "Decimeter" or to_conver == "decimeter" or to_conver == "dm":
            print(f"The result is {num*10}")
        elif to_conver == "Centimeter" or to_conver == "centimeter" or to_conver == "cm":
            print(f"The result is {num * 100}")
        elif to_conver == "Millimeter" or to_conver == "millimeter" or to_conver == "mm":
            print(f"The result is {num * 1000}")
    
    # this will convert the number if from_conver is DeciMeter
    elif from_conver == "Decimeter" or from_conver == "decimeter" or from_conver == "dm":
        if to_conver == "Kilometer" or to_conver == "kilometer" or to_conver == "km":
            print(f"The result is {num/10000} km")
        elif to_conver == "Hectameter" or to_conver == "hectameter" or to_conver == "hm":
            print(f"The result is {num/1000}")
        elif to_conver == "Decameter" or to_conver == "decameter" or to_conver == "dem":
            print(f"The result is {num/100}")
        elif to_conver == "Meter" or to_conver == "meter" or to_conver == "m":
                print(f"The result is {num/10}")
        elif to_conver == "Centimeter" or to_conver == "centimeter" or to_conver == "cm":
            print(f"The result is {num * 10}")
        elif to_conver == "Millimeter" or to_conver == "millimeter" or to_conver == "mm":
            print(f"The result is {num * 100}")


    # this will convert the number if from_conver is CentiMeter
    elif from_conver == "Centimeter" or from_conver == "centimeter" or from_conver == "cm":
        if to_conver == "Kilometer" or to_conver == "kilometer" or to_conver == "km":
            print(f"The result is {num/100000} km")
        elif to_conver == "Hectameter" or to_conver == "hectameter" or to_conver == "hm":
            print(f"The result is {num/10000}")
        elif to_conver == "Decameter" or to_conver == "decameter" or to_conver == "dem":
            print(f"The result is {num/1000}")
        elif to_conver == "Meter" or to_conver == "meter" or to_conver == "m":
                print(f"The result is {num/100}")
        elif to_conver == "Decimeter" or to_conver == "decimeter" or to_conver == "dm":
            print(f"The result is {num/10}")
        elif to_conver == "Millimeter" or to_conver == "millimeter" or to_conver == "mm":
            print(f"The result is {num*10}")
    
    
    # this will convert the number if from_conver is Millimeter
    elif from_conver == "Millimeter" or from_conver == "millimeter" or from_conver == "mm":
        if to_conver == "Kilometer" or to_conver == "kilometer" or to_conver == "km":
            print(f"The result is {num/1000000} km")
        elif to_conver == "Hectameter" or to_conver == "hectameter" or to_conver == "hm":
            print(f"The result is {num/100000}")
        elif to_conver == "Decameter" or to_conver == "decameter" or to_conver == "dem":
            print(f"The result is {num/10000}")
        elif to_conver == "Meter" or to_conver == "meter" or to_conver == "m":
                print(f"The result is {num/1000}")
        elif to_conver == "Decimeter" or to_conver == "decimeter" or to_conver == "dm":
            print(f"The result is {num/100}")
        elif to_conver == "Centimeter" or to_conver == "centimeter" or to_conver == "cm":
            print(f"The result is {num/10}")

converter()