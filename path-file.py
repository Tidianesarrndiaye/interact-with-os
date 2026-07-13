import os

outputs = {}
outputs['current_directory_before'] = os.getcwd()
outputs['files_and_directories'] = os.listdir()
outputs['path_value'] = os.environ.get('PATH')

for key, value in outputs.items():
    print(f"{key}: {value}")
    print("-" * 40)


print(os.path.abspath(__file__))