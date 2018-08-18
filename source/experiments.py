# A string variable
name = 'Hameed'

# A integer varaible
age = 33

# A float variable
height = 1.78

# Printing variables
print(name)
print(age)
print(height)

# Printing variables together
print("%s is my friend, he is %s years old and he is %s meters tall"%(name,age,height))

# A list of names
name_list = ['Hameed', 'Umair', 'Marju']

# A dictionary of names and ages as key value pairs
age_dict = {'Hameed': 33, 'Umair': 30, 'Marju': 28}

# An example of loop with conditional statement
for key in age_dict:
    if age_dict[key] < 30:
        print('This folk %s, is young'%(key))
    else:
        print('This folk %s, is old'%(key))
