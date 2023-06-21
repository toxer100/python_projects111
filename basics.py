stud_grades = ['Mary', "Tod", "Kaster", 10, 22, 9]

print(stud_grades.count(10))

day_temp = {'Day': 10.2, 'Noon': 23.5, 'Evening': 15.8}

print(day_temp.items())

day_temp2 = {'Day': (10.2, 11.5, 2.8), 'Noon': (23.5, 22.55, 4.2), 'Evening': (15.8, 10.2, 33.6)}

print(day_temp2.get('Day'))

color_codes = ((1,2,3), (4,5,6), (7,8,9))

monday_temp = [9.1, 8.4, 3.6]

monday_temp.append(9.14)

print(monday_temp.count(float))

monday_temp.remove(monday_temp[1])

print(monday_temp)

seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)

print(seconds[2:])

moon_slice= ['Epiq', 10, 33.6]

print(moon_slice[0][1])

sunset = {'Day': 6, 'Night': 22}

print(sunset['Day'])

#functions
def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean
    
day_temp = {'Day': 10.2, 'Noon': 23.5, 'Evening': 15.8}
monday_temp = [9.1, 8.4, 3.6]    

print("Index of first item: ", monday_temp.index(9.1))
#print(mean(day_temp))

def give(a):
    return a * a

been = 10

print(give(been))

def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"
    
got = int(input('Enter temperature: '))

print(foo(got))

name1 = "Sim"
experience_years1 = 1.5
gs = '!'
print("Hi %s, you have %s years of experience." % (name1, experience_years1))

name2 = "Tod"
experience_years = 14.5
print(f"Ok, go away {name1} with your {experience_years1} years")
print("Hi {}, you have {} years of experience{}".format(name2, experience_years, gs))


colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)
        
def celsius_to_kelvin(cels):
    return cels + 273.15


monday_temperatures = [9.1, 8.8, -270.15]
for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))
    
    
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for pair in phone_numbers.items():
    print("{} has as phone numb104er {}".format(pair[0], pair[1]))
    
    
for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))
