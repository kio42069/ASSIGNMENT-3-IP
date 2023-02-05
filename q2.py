with open("records.txt", "r") as file:
    records = file.readlines()
string = ""
for i in records:
    string = string + i
