import subprocess

print(subprocess.run(["date"]))
print(subprocess.run(["sleep", "3"]))
result = subprocess.run(["ls", "file_does_not_exist.txt"], capture_output=True, text=True)
