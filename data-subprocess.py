import subprocess

print(subprocess.run(["date"]))

result = subprocess.run(["ls", "file_does_not_exist.txt"], capture_output=True, text=True)
print(result)