def conversion(length):
    to_inch = length / 0.0254
    to_feet = to_inch / 12
    to_yard = to_feet / 3
    to_miles = to_yard / 1760
    print(to_inch)
    print(to_feet)
    print(to_yard)
    print(to_miles)
conversion(640)
