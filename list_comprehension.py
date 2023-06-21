# Python3 program to Find elements of a
# list by indices present in another list
 
def findElements(lst1, lst2):
    return [lst1[i] for i in lst2]
             
# Driver code
lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
print(findElements(lst1, lst2))

# Python3 program to Find elements of a
# list by indices present in another list
 
def findElements1(lst1, lst2):
    return list(map(lst1.__getitem__, lst2))
             
# Driver code
lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
print(findElements1(lst1, lst2))

def findElements2(lst1, lst2):
    # Create a dictionary that maps indices in lst2 to their corresponding elements in lst1
    index_map = {index: element for index, element in enumerate(lst1)}
     
    # Use a list comprehension to extract the values from the dictionary
    return [index_map[index] for index in lst2]
 
lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
print(findElements2(lst1, lst2))

#---------------------
nums = [1,2,3,4,5,6,7,8,9,10]

my_list = []
for letter in "abcd":
  for num in nums:
    my_list.append((letter, num))
    
print(my_list)

my_list = [(letter, num) for letter in "abcd" for num in range(4)]
print(my_list)


temps = [29.3, 20, -100, 60.23, 88, -9999, 122, "no data"]

new_temps = [temp/10 for temp in temps if not(isinstance(temp, str)) and temp > 0]

print(new_temps)

new_temps = [temp/10 if not(isinstance(temp, str)) and temp > 0 else 0 for temp in temps]

print(new_temps)

pair = ['2.3', '2.9', '14.6']

people = [{
  "first_name": "Василий",
  "last_name": "Марков",
  "birthday": "9/25/1984"
}, {
  "first_name": "Регина",
  "last_name": "Павленко",
  "birthday": "8/21/1995"
}]

birthdays = [
  person[term]
  for person in people
  for term in person
  if term == "birthday"
]

print(birthdays)


fruits = ["apples", "bananas", "strawberries"]
fruits = [fruit.upper() for fruit in fruits]

print(fruits)

my_string = "HelloMyNameIsAnton"
my_string = "".join([i if i.islower()  else " " + i.lower() if i in ["N", "I"] else " " + i for i in my_string])[1:]
print(my_string)

numbers = [1,2,3,4,5,6]
letters = ["a","b","c","d","e","f"]
g = {x: y for x, y in zip(numbers, letters)}
print(g)
#---------------------------

def grut(values):
    return sum([float(value) for value in values])

print(grut(pair))


def area(a, b):
    return a+b

print(area('4', '6'))


def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(x=1, y=2, z=6))
