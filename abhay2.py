'''program to print second lowest score of the student
input
    6
    4 5 6 4 3 2
'''

score = input("Give the number of score : ")
string = input("Enter the score : ")
list1=string.split()
unique=[]
for x in list1:
    x=int(x)
    if x not in unique:
        unique.append(int(x))

sort_score = sorted(unique)
print(sort_score[-2])
