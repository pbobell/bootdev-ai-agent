import os

def get_files_info(working_directory, directory="."):
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        absolute_target = os.path.abspath(os.path.join(working_directory, directory))
        #print("abs_workdir:", absolute_working_directory)
        #print("abs_target:", absolute_target)

        if not (absolute_target == absolute_working_directory or absolute_target.startswith(absolute_working_directory + os.sep)):
            #print("Failed working directory bounds check")
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(absolute_working_directory):
            #print(os.path.isdir(absolute_working_directory))
            #print("Failed is-directory check")
            return f'Error: "{absolute_working_directory}" is not a directory'
        
        #print(os.listdir(full_path))    
        #print(os.listdir(full_path)[0])

        #print("Returning:")
        #print("\n".join(list((map(lambda file: f'{file}: file_size={os.path.getsize(f"{absolute_target}/{file}")} bytes, is_dir={os.path.isdir(f"{absolute_target}/{file}")}',os.listdir(absolute_target))))))

        return "\n".join(list((map(lambda file: f'{file}: file_size={os.path.getsize(f"{absolute_target}/{file}")} bytes, is_dir={os.path.isdir(f"{absolute_target}/{file}")}',os.listdir(absolute_target)))))

    except Exception as e:
        print(f"Error: {e}")