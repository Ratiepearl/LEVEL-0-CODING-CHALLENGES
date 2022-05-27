def convert_any_number(number):
 hours = int(number//60)
 minutes = int(number%60)
 if hours > 1 and minutes > 1:
     print(str(hours) + ' hours and ' + str(minutes) + ' minutes ')
 elif hours == 0 and minutes ==0:   
     print(str(hours) + ' hours and ' + str(minutes) + ' minutes ')
 elif hours == 0 and minutes > 1:
     print(str(hours) + ' hours and ' + str(minutes) + ' minutes ')
 elif hours > 1 and minutes == 0:
     print(str(hours) + ' hours and ' + str(minutes) + ' minutes ')  
 elif hours == 0 and minutes == 1:
     print(str(hours) + ' hours and ' + str(minutes) + ' minute ')
 elif hours == 1 and minutes == 0:
      print(str(hours) + ' hour and ' + str(minutes) + ' minutes ')     
 elif hours < 1  and minutes < 1: 
     print(str(hours) + ' hour and ' + str(minutes) + ' minute ')
 elif hours > 1 and minutes < 1:
     print(str(hours) + ' hours and ' + str(minutes) + ' minute ') 
 elif hours < 1 and minutes > 1:
     print(str(hours) + ' hour and ' + str(minutes) + ' minutes ')    
 elif hours == 1 and minutes > 1:
      print(str(hours) + ' hour and ' + str(minutes) + ' minutes ') 
 elif hours > 1 and minutes == 1:
      print(str(hours) + ' hours and ' + str(minutes) + ' minute ')  
 else: 
     print(str(hours) + ' hour and ' + str(minutes) + ' minutes ')       

convert_any_number(-1) 
