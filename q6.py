from time import time 

with open("test.txt", "r") as file:
    xyz = file.readlines()
for i in range(len(xyz)):
    xyz[i] = xyz[i].split()

winner = {"oop" : 0, "dictionary" : 0}
grading_time_oop = 0
grading_time_dictionary = 0
searching_time_oop = 0
searching_time_dictionary = 0
for saldhf in range(100):
    start = time()
    #during new policy creation, if there are two same intervals, we consider only the first interval

    class Course:
        def __init__(self, cname, credits):
            self.cname = cname
            self.credits = credits

    class Student:
        def __init__(self, rollno, labs, midsem, assignments, endsem, labs_total, midsem_total, assignments_total, endsem_total, assessments):
            self.rollno = rollno
            for i in assessments:
                if i[0] == "labs":
                    self.labs = (labs/labs_total)*(i[1])
                elif i[0] == "midsem":
                    self.midsem = (midsem/midsem_total)*(i[1])
                elif i[0] == "assignments":
                    self.assignments = (assignments/assignments_total)*(i[1])
                else:
                    self.endsem = (endsem/endsem_total)*(i[1])
            self.marks = self.labs+self.midsem+self.assignments+self.endsem
            
        def set_grade(self,grade):
            self.grade = grade

    cname = "IP"
    credits = 4
    assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
    policy = [80,65,50,40]
    grade_names = ['A','B','C','D','F']
    course = Course(cname, credits)
    student_list = []
    for i in xyz:
        roll = int(i[0])
        labs, labs_total = int(i[1]), int(i[2])
        midsem, midsem_total = int(i[3]), int(i[4])
        assignments, assignments_total= int(i[5]), int(i[6])
        endsem, endsem_total =  int(i[7]), int(i[8])
        student = Student(rollno=roll, assignments=assignments,labs=labs, midsem=midsem, endsem=endsem, labs_total = labs_total, midsem_total=midsem_total, assignments_total=assignments_total, endsem_total=endsem_total, assessments=assessments)
        student_list.append(student)
    with open("marks.txt","w") as file:
        file.write("Roll No.\tMarks\n")
        for student in student_list:
            record = str(student.rollno)+"\t\t"+str(student.marks)+"\n"
            file.write(record)


    cutoffs_final = policy.copy()
    for i in range(len(policy)):
        try:
            markes = []
            for student in student_list:
                if student.marks >= policy[i]-2 and student.marks <= policy[i]+2:
                    markes.append(student.marks)
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
    for student in student_list:
        if student.marks >= cutoffs_final[0]:
            student.set_grade(grade_names[0])
            grade_count[grade_names[0]] += 1
        elif student.marks >= cutoffs_final[1]:
            student.set_grade(grade_names[1])
            grade_count[grade_names[1]] += 1
        elif student.marks >= cutoffs_final[2]:
            student.set_grade(grade_names[2])
            grade_count[grade_names[2]] += 1
        elif student.marks >= cutoffs_final[3]:
            student.set_grade(grade_names[3])
            grade_count[grade_names[3]] += 1
        elif student.marks >= cutoffs_final[4]:
            student.set_grade(grade_names[4])
            grade_count[grade_names[4]] += 1


    def summary():
        x = (f"Course name : {course.cname}")
        x = (f"Total credits : {course.credits}")
        for i in assessments:
            x = (f"Assesment type : {i[0]}\tWeightage : {i[1]}")
        x = ("\nCutoffs")
        for i in range(len(cutoffs_final)):
            x = (f"{grade_names[i]} : {cutoffs_final[i]}")
        x = ("Grade counts")
        for i in grade_count:
            x = (f"{i} : {grade_count[i]}")
        
    def upload():
        with open("grades.txt","w") as file:
            for i in student_list:
                file.write(f"{i.rollno} {i.marks} {i.grade}\n")
        

    def search(roll_number):
        for student in student_list:
            if student.rollno == roll_number:
                x = (f"RECORD FOR ROLL NUMBER : {roll_number}")
                x = ()
                x = (f"Lab marks : {student.labs}")
                x = (f"Midsem marks : {student.midsem}")
                x = (f"Assignments marks : {student.assignments}")
                x = (f"Endsem marks : {student.endsem}")
                x = ()
                x = (f"Grade recieved : {student.grade}")
                break
        
    for i in range(1,4):
        x = ("Enter")
        x = ("1. Generate course summary")
        x = ("2. Student grades")
        x = ("3. Search student records")
        user = i
        if user == 1:
            summary()
        elif user == 2:
            s = time()
            upload()
            e = time()
            grading_time_oop += e-s
        elif user == 3:
            roll_number = 43
            s = time()
            search(roll_number)
            e = time()
            searching_time_oop += e-s
        else:
            break
    end = time()
    time1 = (end-start)
    start = time()
    cname = "IP"
    credits = 4
    assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
    policy = [80,65,50,40]
    grade_names = ['A','B','C','D','F']

    students = []
    courses = dict()

    courses[cname] = credits

    for j in xyz:
        roll = int(j[0])
        labs, labs_total = int(j[1]), int(j[2])
        midsem, midsem_total = int(j[3]), int(j[4])
        assignments, assignments_total= int(j[5]), int(j[6])
        endsem, endsem_total =  int(j[7]), int(j[8])

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
        students.append({"rollno":roll, "assignments":assignments, "labs":labs, "midsem":midsem, "endsem" :endsem, "labs_total":labs_total, "midsem_total":midsem_total, "assignments_total":assignments_total, "endsem_total":endsem_total, "assessments":assessments, "marks":marks})
    with open("marks.txt","w") as file:
        file.write("Roll No.\tMarks\n")
        for student in students:
            record = str(student["rollno"])+"\t\t"+str(student["marks"])+"\n"
            file.write(record)


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
        x = (f"Course name : {cname}")
        x = (f"Total credits : {credits}")
        for i in assessments:
            x = (f"Assesment type : {i[0]}\tWeightage : {i[1]}")
        x = ("\nCutoffs")
        for i in range(len(cutoffs_final)):
            x = (f"{grade_names[i]} : {cutoffs_final[i]}")
        x = ("Grade counts")
        for i in grade_count:
            x = (f"{i} : {grade_count[i]}")


    def upload():
        with open("grades.txt","w") as file:
            for i in students:
                file.write(f"{i['rollno']} {i['marks']} {i['grade']}\n")

    def search(roll_number):
        for student in students:
            if student['rollno'] == roll_number:
                x = (f"RECORD FOR ROLL NUMBER : {roll_number}")
                x = ()
                x = (f"Lab marks : {student['labs']}")
                x = (f"Midsem marks : {student['midsem']}")
                x = (f"Assignments marks : {student['assignments']}")
                x = (f"Endsem marks : {student['endsem']}")
                x = ()
                x = (f"Grade recieved : {student['grade']}")
                break

    for i in range(1,3):
        x = ("Enter")
        x = ("1. Student grades")
        x = ("2. Search student records")
        user = i
        if user == 1:
            summary()
        elif user == 2:
            s = time()
            upload()
            e = time()
            grading_time_dictionary += e-s
        elif user == 3:
            roll_number = 43
            s = time()
            search(roll_number)
            e = time()
            searching_time_dictionary += e-s
        else:
            break
    end = time()
    time2 = (end-start)
    if time1>time2:
        winner["dictionary"] += 1
    else:
        winner["oop"] += 1
print(winner)
print(grading_time_dictionary)
print(grading_time_oop)
print(searching_time_dictionary)
print(searching_time_oop)