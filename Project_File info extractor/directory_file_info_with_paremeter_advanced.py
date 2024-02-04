# Import the os module for interacting with the operating system
import os

# Define a function to get information about files in a directory (recursively).
def get_recursive_file_information(input_directory="."):
    # Initialize an empty dictionary to store file information
    information_dict = {}

    # Get a list of files and directories in the specified directory
    files_and_dirs = os.listdir(input_directory)

    # Iterate through each file or directory
    for item_name in files_and_dirs:
        # Create the full path by joining the directory and item name
        item_path = os.path.join(input_directory, item_name)

        if os.path.isfile(item_path):
            # If it's a file, add file information to the dictionary
            file_size = os.path.getsize(item_path)
            information_dict[item_name] = {'path': item_path, 'size': file_size}
        elif os.path.isdir(item_path):
            # If it's a directory, recursively call the function to get information for subdirectories
            subdirectory_info = get_recursive_file_information(item_path)
            information_dict[item_name] = subdirectory_info

    return information_dict

# Function to get user input for directory path or use the current directory as default
def get_user_input_path():
    user_input = input("Enter the directory path (press Enter to use the current directory): ")
    return user_input.strip() or "."

# Function to print recursive file information for a specified directory (defaulting to the working directory)
def print_recursive_file_information():
    # Get user input for the directory path or use the current directory as default
    user_input_path = get_user_input_path()

    # Call the function to get recursive file information for the specified or default directory
    files_info_result = get_recursive_file_information(user_input_path)

    # Print the recursive file information
    print(files_info_result)

# Call the function to print recursive file information, prompting the user for input
print_recursive_file_information()

