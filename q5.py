cname = input("Enter course name: ")
credits = int(input("Enter number of credits: "))
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
policy = [80,65,50,40]
grade_names = ['A','B','C','D','F']

students = []
courses = dict()

courses[cname] = credits

while True:
    try:
        roll = int(input("Enter roll number: "))
        labs, labs_total = map(int,input("Enter lab score and total marks: ").split())
        midsem, midsem_total = map(int,input("Enter midsem score and total marks: ").split())
        assignments, assignments_total= map(int,input("Enter assignments score and total marks: ").split())
        endsem, endsem_total =  map(int,input("Enter endsem score and total marks: ").split())
        
        for i in assessments:
            if i[0] == "labs":
                labs = (labs/labs_total)*(i[1])
            elif i[0] == "midsem":
                midsem = (midsem/midsem_total)*(i[1])
            elif i[0] == "assignments":
                assignments = (assignments/assignments_total)*i[1]
            else:
                endsem = (endsem/endsem_total)*i[1]
        marks = labs+midsem+assignments+endsem
        students.append({"rollno":roll, "assignments":assignments, "labs":labs, "midsem":midsem, "endsem" : endsem, "labs_total":labs_total, "midsem_total":midsem_total, "assignments_total":assignments_total, "endsem_total":endsem_total, "assessments":assessments, "marks":marks})
    except:
        with open("marks.txt","w") as file:
            file.write("Roll No.\tMarks\n")
            for student in students:
                record = str(student["rollno"])+"\t\t"+str(student["marks"])+"\n"
                file.write(record)
        break
    

cutoffs_final = policy.copy()
for i in range(len(policy)):
    try:
        markes = []
        for student in students:
            if student["marks"] >= policy[i]-2 and student["marks"] <= policy[i]+2:
                markes.append(student["marks"])
        markes.sort(reverse=True)
        differences = []
        for j in range(len(markes)-1):
            differences.append(markes[i]-markes[i+1])
        index = differences.index(max(differences))
        index_next = index + 1
        cutoffs_final[i] = (markes[index]+markes[index+1])/2
    except:
        continue
    

grade_count = {key:0 for key in grade_names}
for student in students:
    if student["marks"] >= cutoffs_final[0]:
        student["grade"] = grade_names[0]
        grade_count[grade_names[0]] += 1
    elif student["marks"] >= cutoffs_final[1]:
        student["grade"] = grade_names[1]
        grade_count[grade_names[1]] += 1
    elif student["marks"] >= cutoffs_final[2]:
        student["grade"] = grade_names[2]
        grade_count[grade_names[2]] += 1
    elif student["marks"] >= cutoffs_final[3]:
        student["grade"] = grade_names[3]
        grade_count[grade_names[3]] += 1
    elif student["marks"] >= cutoffs_final[4]:
        student["grade"] = grade_names[4]
        grade_count[grade_names[4]] += 1



def summary():
    print(f"Course name : {cname}")
    print(f"Total credits : {credits}")
    for i in assessments:
        print(f"Assesment type : {i[0]}\tWeightage : {i[1]}")
    print("\nCutoffs")
    for i in range(len(cutoffs_final)):
        print(f"{grade_names[i]} : {cutoffs_final[i]}")
    print("Grade counts")
    for i in grade_count:
        print(f"{i} : {grade_count[i]}")


def upload():
    with open("grades.txt","w") as file:
        for i in students:
            file.write(f"{i['rollno']} {i['marks']} {i['grade']}\n")

def search(roll_number):
    for student in students:
        if student['rollno'] == roll_number:
            print(f"RECORD FOR ROLL NUMBER : {roll_number}")
            print()
            print(f"Lab marks : {student['labs']}")
            print(f"Midsem marks : {student['midsem']}")
            print(f"Assignments marks : {student['assignments']}")
            print(f"Endsem marks : {student['endsem']}")
            print()
            print(f"Grade recieved : {student['grade']}")
            break
    
while True:
    print("Enter")
    print("1. Generate course summary")
    print("2. Student grades")
    print("3. Search student records")
    user = int(input())
    if user == 1:
        summary()
    elif user == 2:
        upload()
    elif user == 3:
        roll_number = int(input("Enter roll number to be searched: "))
        search(roll_number)
    else:
        break