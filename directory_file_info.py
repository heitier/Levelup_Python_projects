import os

def get_file_information(input_directory="."):
    information_list = []

    files_in_directory = os.listdir(input_directory)

    for file_name in files_in_directory:
        file_path = os.path.join(input_directory, file_name)
        file_size = os.path.getsize(file_path)
        file_data = {'name': file_name, 'path': file_path, 'size': file_size}
        information_list.append(file_data)

    return information_list

files_info_result = get_file_information()
for file_data_result in files_info_result:
    print(file_data_result)
