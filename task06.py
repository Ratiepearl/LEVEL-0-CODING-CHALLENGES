def maximum_number(number1,number2,number3):
    if number2 <= number1 >= number3:
        return(number1)
    elif number1 <= number2 >= number3:
        return(number2)   
    elif number1 <= number3 >= number2:
        return(number3)      
print(maximum_number(10,510,200))        