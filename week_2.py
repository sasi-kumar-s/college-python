#1st code of week 2
for num in range(20,50):     
 for i in range(2,num):         
   if num%i == 0:  
     break     
 else:  
   print (num, 'is a prime number') 

#2nd code of week 2
a = int(input('enter number: '))
b = int(input('enter number: 5')) 
x = lambda a, b : a + b 
print('sum of two number is ', x(a, b))  
