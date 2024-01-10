"""
This program generates a random unique EC2 name in shared AWS environment across multiple departments 

"""
import random
import string

# is_quantity = int (input("How many EC2 Instances do you want? "))
# is_department_name = input("What's the name of your department? ")
# is_date = input("What Month is it? ")
# is_year = input("What year is it? ")
# n = 0
# # Naming convention is department name-characters

# def generate_random_character(size=7, all_characters=None):
#  all_characters = random.choice(string.ascii_letters) + random.choice(string.ascii_uppercase) + random.choice(string.punctuation) + random.choice(string.digits)
#  return ''.join(all_characters)

# while n < is_quantity:
#   print(is_department_name,is_year,generate_random_character(),'_',is_date,'_',is_year,generate_random_character(), sep='')
#   n += 1
  
  
# def generate_random_character(size=7, all_characters=None):
#  all_characters = random.choice(string.ascii_letters) + random.choice(string.ascii_uppercase) + random.choice(string.punctuation) + random.choice(string.digits)
#  return ''.join(all_characters)
    

# def generate_random_character(size=7, all_characters = string.ascii_letters + string.ascii_uppercase + string.punctuation + string.digits):
#   """Generates a random character."""

#  # all_characters = string.ascii_letters + string.ascii_uppercase + string.punctuation + string.digits
#   return ''.join(random.choice(all_characters) for _ in range(size))

# print(generate_random_character())



# print(generate_random_character())

def generate_ec2_instance_name(quantity, department_name, month, year):
    instance_names = []
    acceptable_department = ['accounting', 'marketing', 'finops']
    
    if is_department_name.lower() in acceptable_department:
     for _ in range(quantity):
      random_characters = random.choice(string.ascii_letters) + random.choice(string.ascii_uppercase) + random.choice(string.punctuation) + random.choice(string.digits)
      instance_name = f"{year}{month}_{department_name}{random_characters}"
      instance_names.append(instance_name)
      
     return instance_names
    else:
     return "none"
     

# Input
is_quantity = int(input("How many EC2 Instances do you want? "))
is_department_name = input("What's the name of your department? ")
is_date = input("What Month is it? ")
is_year = input("What year is it? ")

# Generate EC2 instance names
generated_names = generate_ec2_instance_name(is_quantity, is_department_name, is_date, is_year)

# Display the generated names
print("Generated EC2 Instance Names:")
for name in generated_names:
    print(name)
