import os

if os.path.exists("path-file.py"):
    print("File still exists.")
    os.rename("path-file.py", "renamed-path-file.py")
    