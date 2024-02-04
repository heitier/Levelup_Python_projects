# Import the os module for interacting with the operating system
import os

# Define a function to get information about files in a directory
def get_file_information(input_directory="."):
    # Initialize an empty list to store file information
    information_list = []

    # Get a list of files in the specified directory
    files_in_directory = os.listdir(input_directory)

    # Iterate through each file in the directory
    for file_name in files_in_directory:
        # Create the full file path by joining the directory and file name
        file_path = os.path.join(input_directory, file_name)

        # Get the size of the file
        file_size = os.path.getsize(file_path)

        # Create a dictionary with file information and append it to the list
        file_data = {'name': file_name, 'path': file_path, 'size': file_size}
        information_list.append(file_data)

    # Return the list of file information
    return information_list

# Call the function to get file information for the current directory
files_info_result = get_file_information()

# Iterate through the list of file information and print each entry
for file_data_result in files_info_result:
    print(file_data_result)
