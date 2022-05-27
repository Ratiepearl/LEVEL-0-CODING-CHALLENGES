from tempfile import tempdir


def temp_celsius(number_celsius):
    fahrenheit = (number_celsius + 9/5) + 32
    return(fahrenheit)   
print('Temperature in fahrenheit: ',temp_celsius(0))    
def temp_fahrenheit(number_fahrenheit):
    celsius = (number_fahrenheit-32) * 5/9
    return(celsius)
print('Temperature in celsius: ',temp_fahrenheit(6))