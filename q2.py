with open("records.txt", "r") as file:
    records = file.readlines()
processed_records = []
for i in records:
    processed_records.append(i.split(", "))
    
for i in range(len(processed_records)):
    processed_records[i][-1] = int(processed_records[i][-1][0:2])*60*60+int(processed_records[i][-1][3:5])*60+int(processed_records[i][-1][6:8])
    