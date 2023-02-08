with open("records.txt", "r") as file:
    records = file.readlines()
processed_records = []
for i in records:
    processed_records.append(i.split())
