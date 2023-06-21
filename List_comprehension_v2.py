matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
flattened = [num for row in matrix for num in row] 
print(flattened)
# Output : flattened = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

# 2. Filter odd and even numbers from a list using conditionals: 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = [num for num in numbers if num % 2 == 1] 
even = [num for num in numbers if num % 2 == 0] 
# Output : odd = [1, 3, 5, 7, 9], even = [2, 4, 6, 8, 10] ```  

# 3. Create a dictionary from two lists using zipping: 
names = ['Alice', 'Bob', 'Charlie', 'Dave'] 
ages = [25, 30, 35, 40] 
person_dict = {name:age for name, age in zip(names, ages)} 
# Output : person_dict = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'Dave': 40}

# 4. Generate a list of tuples from two lists using nested zip and conditionals:
fruits = ['apple', 'banana', 'orange', 'pineapple'] 
quantities = [3, 1, 2, 4] 
fruit_list = [(fruit, quantity) for fruit, quantity in zip(fruits, quantities) if quantity > 2] 
# Output : fruit_list = [('apple', 3), ('pineapple', 4)] 

# 5. Find common elements between two lists using set comprehensions:
list1 = [1, 2, 3, 4, 5] 
list2 = [1, 3, 5, 7, 9] 
common = {num for num in list1 if num in list2} 
print(common)
# Output : common = {1, 3, 5} 


#1. Square of even numbers from 1 to 10 
squares = [num**2 for num in range(1, 11) if num % 2 == 0] 
print(squares)    
# Output: [4, 16, 36, 64, 100] 

# 2. Vowels in a string ``` 
string = "hello world" 
vowels = [char for char in string if char in 'aeiou'] 
print(vowels)    
# Output: [\'e\', \'o\', \'o\']

# 3. Flatten a nested list
nested_list = [[1,2,3], [4,5,6], [7,8,9]] 
flattened_list = [val for sublist in nested_list for val in sublist] 
print(flattened_list)    
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4. Length of words in a sentence
sentence = "This is a sample sentence" 
lengths = [len(word) for word in sentence.split()] 
print(lengths)    
# Output: [4, 2, 1, 6, 8]

# 5. Sum of numbers in a list 
numbers = [1, 2, 3, 4, 5] 
sum = sum([num for num in numbers]) 
print(sum)    
# Output: 15


#
def has_duplicates(lst):
    return len(lst) != len(set(lst))

x = [1,2,3,4,5,5]
y = [1,2,3,4]

print(has_duplicates(y))