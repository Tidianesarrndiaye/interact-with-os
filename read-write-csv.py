import csv

print("-"*50)
with open("sample-data/csv_file.txt", "r") as f:
    csv_f = csv.reader(f)
    print("Reading CSV file...")
    for row in csv_f:
        name, phone, role = row
        print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
    print("Done reading CSV file.")
print("-"*50)
    
print("Writing to CSV file hosts.csv...")
hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('sample-data/hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
print("Done writing to CSV file hosts.csv.")

print("-"*50)
print("Reading CSV file software.csv with DictReader...")
with open('sample-data/software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
      print(("{} has {} users").format(row["name"], row["users"]))

print("Done reading CSV file software.csv.")

print("-"*50)
print("Writing to CSV file by_department.csv with DictWriter...")
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('sample-data/by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
print("Done writing to CSV file by_department.csv.")
