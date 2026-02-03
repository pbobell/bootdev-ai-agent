import os
from config import MAX_CHARACTERS

def get_file_content(working_directory, file_path):
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        absolute_target = os.path.abspath(os.path.join(working_directory, file_path))
        print(f"working_directory: {absolute_working_directory}")
        print(f"file_path: {absolute_target}")
        
        if not (absolute_target == absolute_working_directory or absolute_target.startswith(absolute_working_directory + os.sep)):
            #print("Failed working directory bounds check")
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not (os.path.isfile(absolute_target)):
            f'Error: File not found or is not a regular file: "{file_path}"'

        with open(absolute_target, "r") as f:
            file_content_string = f.read(MAX_CHARACTERS)

        return str(file_content_string)

    except Exception as e:
        print(f"Error: {e}")
