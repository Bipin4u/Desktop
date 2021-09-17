'''program to take student same and score and sort then in order by name'''

while(True):
    try:
        no_of_student=int(input("Enter the number of student: "))
        break
    except:
        print("Please give a integer value")

        continue

student_score=[]
dummy_score=list()
for _ in range(no_of_student):
    print()
    name = input("Enter the name of the student: ")
    while(True):
        try:
            score= float(input("Enter the score of the student: "))
            break
        except:
            print("please enter a numerical value")
            print("Re-enter the student details")
            continue
    student_score.append([name,score])

orderedlist = sorted(student_score, key=lambda x:x[0])
print()
print("The order of the student according to name is :")
[print(_) for _ in orderedlist]
orderedscore = sorted(student_score, key=lambda x:x[1])


list=[]

for _ in orderedscore:
    if _[1] in list:
        continue
    list.append(_[1])
try:
    second_least_number = list[1]
except:
    print("Every one has scored same grade")
    second_least_number=list[0]
print()
print("Second lowest grade student are: ")
for _ in orderedlist:
    if second_least_number in _:
        print(_)
