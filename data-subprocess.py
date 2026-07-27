import subprocess

print(subprocess.run(["date"]))
print(subprocess.run(["sleep", "3"]))
result = subprocess.run(["ls", "file_does_not_exist.txt"])
print(result)
print("Return code:", result.returncode)


print("-"*50)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)



result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)



result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)



result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split())



print("-"*50)

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr) #ici on voit bien que stderr est différent de stdout, il contient le message d'erreur de la commande rm