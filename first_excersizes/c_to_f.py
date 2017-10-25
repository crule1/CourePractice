def cel_to_fahr(cel):
    fahr = cel * 9.0 / 5.0 + 32.0
    return fahr


celsius = float(input("Enter degrees in Celsius:"))
fahrenheit = cel_to_fahr(celsius)
print("That is {0} Fahrenheit".format(round(fahrenheit,1)))
