import os

def run_python_file(working_directory, file_path, args=[]):
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        absolute_target = os.path.abspath(os.path.join(working_directory, file_path))
        print(f"working_directory: {absolute_working_directory}")
        print(f"file_path: {absolute_target}")
        
        if not (absolute_target == absolute_working_directory or absolute_target.startswith(absolute_working_directory + os.sep)):
            #print("Failed working directory bounds check")
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not (os.path.isfile(absolute_target)):
            return f'Error: File "{file_path}" not found.'
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file.'

        with open('my_file.txt', 'w') as f:
        #    f.write(content)
            pass

        #return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        pass

    except Exception as e:
        print(f"Error: {e}")