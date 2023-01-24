matrix = []
with open("linalg.txt","r") as file:
    rows = file.readline()
    columns = file.readline()
    while True:
        record = file.readline()
        if record != "":
            record = list(map(int,record.split()))
            matrix.append(record)
        else:
            break

print(matrix) 