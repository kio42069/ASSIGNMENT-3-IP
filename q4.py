#during new policy creation, if there are two same intervals, we consider only the first interval

class Course:
    def __init__(self, cname, credits):
        self.cname = cname
        self.credits = credits
        print("Course created")

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

cname = input("Enter course name: ")
credits = int(input("Enter number of credits: "))
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
policy = [80,65,50,40]
grade_names = ['A','B','C','D','F']
course = Course(cname, credits, assessments, policy)
student_list = []
while True:
    try:
        roll = int(input("Enter roll number: "))
        labs, labs_total = map(int,input("Enter lab score and total marks: ").split())
        midsem, midsem_total = map(int,input("Enter midsem score and total marks: ").split())
        assignments, assignments_total= map(int,input("Enter assignments score and total marks: ").split())
        endsem, endsem_total =  map(int,input("Enter endsem score and total marks: ").split())
        student = Student(rollno=roll, assignments=assignments,labs=labs, midsem=midsem, endsem=endsem, labs_total = labs_total, midsem_total=midsem_total, assignments_total=assignments_total, endsem_total=endsem_total, assessments=assessments)
        student_list.append(student)
    except:
        with open("marks.txt","w") as file:
            file.write("Roll No.\tMarks\n")
            for student in student_list:
                record = str(student.rollno)+"\t\t"+str(student.marks)+"\n"
                file.write(record)
        break


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
    print(f"Course name : {course.cname}")
    print(f"Total credits : {course.credits}")
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
        for i in student_list:
            file.write(f"{i.rollno} {i.marks} {i.grade}\n")
    

def search(roll_number):
    for student in student_list:
        if student.rollno == roll_number:
            print(f"RECORD FOR ROLL NUMBER : {roll_number}")
            print()
            print(f"Lab marks : {student.labs}")
            print(f"Midsem marks : {student.midsem}")
            print(f"Assignments marks : {student.assignments}")
            print(f"Endsem marks : {student.endsem}")
            print()
            print(f"Grade recieved : {student.grade}")
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