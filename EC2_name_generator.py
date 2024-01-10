"""
This program generates a random unique EC2 name in shared AWS environment across multiple departments 

"""
import random
import string

def generate_ec2_instance_name(quantity, department_name, month, year):
    # Initialize an empty list to store generated instance names
    instance_names = []
    
    # Generate EC2 instance names based on the specified quantity
    for _ in range(quantity):
        # Create a random string of characters using various character sets
        random_characters = (
            random.choice(string.ascii_letters) +
            random.choice(string.ascii_uppercase) +
            random.choice(string.punctuation) +
            random.choice(string.digits)
        )
        
        # Combine year, month, department name, and random characters to form the instance name
        # Our naming convention example: Year+Month_Department name+random characters+number
        
        instance_name = f"{year}{month}_{department_name}{random_characters}"
        
        # Append the generated instance name to the list
        instance_names.append(instance_name)
     
    # Return the list of generated instance names
    return instance_names

# User input for EC2 instance generation
is_quantity = int(input("How many EC2 Instances do you want? "))
is_department_name = input("What's the name of your department? ")
is_date = input("What Month is it? ")
is_year = input("What year is it? ")

# List of acceptable department names
acceptable_departments = ['accounting', 'marketing', 'finops']

# Generate EC2 instance names
generated_names = generate_ec2_instance_name(is_quantity, is_department_name, is_date, is_year)

# Display the generated names based on department validity
if is_department_name.lower() in acceptable_departments:
    print("Generated EC2 Instance Names:")
    for name in generated_names:
        print(name)
else:
    print(f"Your department ({is_department_name}) is not among the following list: {acceptable_departments}. Hence you can't use the Name Generator.")
