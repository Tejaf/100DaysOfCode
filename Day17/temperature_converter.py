def celsius_to_farenheit(c):
    f = (c * 9.0/5 ) + 32
    return round(f, 2)

def fahrenheit_to_celsius(f):
    c = (f - 32) * 5.0/9
    return round(c, 2)




print celsius_to_farenheit(-2)
print fahrenheit_to_celsius(28.4)