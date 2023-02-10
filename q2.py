with open("records.txt", "r") as file:
    records = file.readlines()
processed_records = []
records.pop(0)
for i in records:
    processed_records.append(i.split(", "))
    
for i in range(len(processed_records)):
    processed_records[i][-1] = int(processed_records[i][-1][0:2])*60*60+int(processed_records[i][-1][3:5])*60+int(processed_records[i][-1][6:8])
processed_records = sorted(processed_records, key = lambda x: x[3]) 

def convert_to_dict(data):
    records = {}
    for entry in data:
        student_name, crossing, gate_number, time = entry.strip().split(',')
        if student_name not in records:
            records[student_name] = {'entries': [], 'exits': []}
        records[student_name]['entries' if crossing == 'ENTER' else 'exits'].append((gate_number, time))
    return records

def query_student_records(student_name, records, current_time):
    student_record = records.get(student_name)
    if not student_record:
        print(f"No record found for student: {student_name}")
        return

    entries = student_record['entries']
    exits = student_record['exits']
    present_in_campus = False
    if entries and not exits:
        present_in_campus = True
        exits = [('N/A', 'N/A')]
    elif exits and not entries:
        entries = [('N/A', 'N/A')]
    elif entries and exits:
        entry_time = entries[0][1]
        exit_time = exits[-1][1]
        if entry_time < current_time < exit_time:
            present_in_campus = True

    print(f"Record for student: {student_name}")
    print(f"Entries: {entries}")
    print(f"Exits: {exits}")
    print(f"Present in campus: {'Yes' if present_in_campus else 'No'}")

def query_students_by_time(start_time, end_time, records):
    entered_students = []
    exited_students = []
    for student_name, record in records.items():
        entries = record['entries']
        exits = record['exits']
        for entry in entries:
            if start_time <= entry[1] <= end_time:
                entered_students.append((student_name, 'ENTER', entry[0], entry[1]))
        for exit in exits:
            if start_time <= exit[1] <= end_time:
                exited_students.append((student_name, 'EXIT', exit[0], exit[1]))
    print(f"Entered students between {start_time} and {end_time}:")
    for entry in entered_students:
        print(','.join(entry))
    print(f"Exited students between {start_time} and {end_time}:")
    for exit in exited_students:
        print(','.join(exit))

def query_gate_record(gate_number, records):
    entered_count = 0
    exited_count = 0
    for record in records.values():
        entries = record['entries']
        exits = record['exits']
        for entry in entries:
            if entry[0] == gate_number:
                entered_count += 1
        for exit in exits:
            if exit[0] == gate_number:
                exited_count += 1
   

while True:
    user = int(input("Enter\n1. Search student records\n2. Search student records by time\n3. Search gate records: "))
    if user == 1:
        query_student_records()
    elif user == 2:
        query_students_by_time()
    elif user == 3:
        query_gate_record()
    else:
        break