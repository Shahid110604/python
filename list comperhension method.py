'''numbers=[10,20,30,40,50]
double_numbers=[num*2 for num in numbers]
print(double_numbers)'''


'''numbers=[10,20,30,40,50]
square_numbers=[]
for num in numbers:
    square_numbers.append(num*num)
    
print(square_numbers)'''


numbers=[10,20,30,40,50]
# creat a list using list comprehension
square_numbers=[num*num for num in numbers]
print(square_numbers)


#conditionals in list comprehension
#[expression for item in list if condition == True]
#filtering even numbers from a list
even_numbers=[num for num in range(1,10) if num%2==0]
print(even_numbers)
# output :[2,4,6,8]

word ="shahid"
vowels = "aeiou"

#find vowel in the string "shahid"
result = [char for char in word if char in vowels]
print(result)