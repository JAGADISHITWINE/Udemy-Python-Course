#Fahrenheit  = (Temperature in degrees Celcius (C) * 9/5) + 32

celsius_temperature = [25,30,15,10,35]

def fahrenheit(c):
    return (c * (9/5)) + 32

Fahrenheit = list(map(fahrenheit,celsius_temperature))
print(Fahrenheit)