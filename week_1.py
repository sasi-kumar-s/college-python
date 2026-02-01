#1st code of week 1
numbers = [10, 5, 3, 8, 15, 2]
length_of_list = len(numbers)
print("Length of the list:", length_of_list) 
maximum_value = max(numbers)  
print("Maximum value in the list:", maximum_value) 
minimum_value = min(numbers)  
print("Minimum value in the list:", minimum_value) 
total_sum = sum(numbers) 
print("Sum of all elements in the list:", total_sum) 
sorted_list = sorted(numbers)  
print("Sorted list:", sorted_list) 
print("\n")

#2nd code of week 1
member1 = ("sasi", 18, "arilova,vizag", "gvp")
member2 = ("sasi kumar", 18, "mvp,vizag", "gvp") 
concatenated_tuples = member1 + member2 
print(f"concatenated_tuples : {concatenated_tuples}\n")  

#3rd code of week 1
str1 = input("Enter a string: ")  
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} 
count = 0  
for char in str1:     
   if char in vowels:         
    count += 1  
print("Number of vowels:", count)

#4th code of week 1
details = { 'name': 'abhishek','age': 22, 'marks':98 }  
print("Existing Dictionary:",details)  
new_key = input("Enter the new key: ")  
new_value = input("Enter the new value: ")  
details[new_key] = new_value  
print("Updated Dictionary:",details) 
