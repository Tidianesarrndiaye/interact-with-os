with open("spider.txt") as file:
	print(file.readline())
	print(file.readline())
	print(file.readline())
	print(file.read())
print("--------------------------")
with open("spider.txt") as file:
	for line in file:
		print(line.upper(), end="")
	
print("--------------------------")
with open("spider.txt") as file:
	lines = file.readlines()


with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

print(lines)
		