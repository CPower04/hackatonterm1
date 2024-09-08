
import csv
import time
def get_info_by_id(csv_file, student_id):
    user_info = []
    with open(csv_file, 'r') as file:
        for line in file:
            fields = line.strip().split(',')
            if fields[0] == student_id:
                user_info = fields
                break
    return user_info

csv_file = r"C:\Users\conor\OneDrive - University of Limerick\hackaton\cs4222_students_list.csv"


davidID = "#23383747"
conorID = "#23369779"
markID = "#23361972"
francisID = "#23374268"
alexID = "#23388439"

davidInfo = get_info_by_id(csv_file, davidID)
francisInfo = get_info_by_id(csv_file, francisID)
conorInfo = get_info_by_id(csv_file, conorID)
markInfo = get_info_by_id(csv_file, markID)
alexInfo = get_info_by_id(csv_file, alexID)

names = [davidInfo[2], francisInfo[2], conorInfo[2], markInfo[2], alexInfo[2]]

CS4221 = "Foundations of Computer Science 1"
CS4222 = "Software Development"
CS4141 = "Introduction to Programming"

CS4221_scores = [17, 34, 65, 77, 2]
CS4222_scores = [50, 42, 0, 100, 88]
CS4141_scores = [8, 30, 18, 27, 60]

davidInfo.append([CS4221, "CS4221", CS4221_scores[0]])
davidInfo.append([CS4222, "CS4222", CS4222_scores[0]])
davidInfo.append([CS4141, "CS4141", CS4141_scores[0]])

francisInfo.append([CS4221, "CS4221",CS4221_scores[1]])
francisInfo.append([CS4222, "CS4222",CS4222_scores[1]])
francisInfo.append(CS4141_scores[1])

conorInfo.append([CS4221, "CS4221",CS4221_scores[2]])
conorInfo.append([CS4222, "CS4222",CS4222_scores[2]])
conorInfo.append([CS4222, "CS4222", CS4141_scores[2]])

markInfo.append([CS4221, "CS4221",CS4221_scores[3]])
markInfo.append([CS4222, "CS4222",CS4222_scores[3]])
markInfo.append([CS4222, "CS4222",CS4141_scores[3]])

alexInfo.append([CS4221, "CS4221",CS4221_scores[4]])
alexInfo.append([CS4222, "CS4222",CS4222_scores[4]])
alexInfo.append([CS4222, "CS4222",CS4141_scores[4]])

print(davidInfo)
print(francisInfo)
print(conorInfo)
print(markInfo)
print(alexInfo)


copyCS4222=(CS4222_scores)
copyCS4221 = (CS4221_scores)
copyCS4141 =(CS4141_scores)
copyNAMES =(names)


topscoreCS4221list = []
topscoreCS4222list = []
topscoreCS4141list = []

start=time.time()
i = 0
for i in copyCS4141:
    index = copyCS4141.index(max(copyCS4141))
    topscoreCS4141list.append(copyNAMES[index])
    copyCS4141[index]= 0

for i in copyCS4221:
    index = copyCS4221.index(max(copyCS4221))
    topscoreCS4221list.append(copyNAMES[index])
    copyCS4221[index]= 0

for i in copyCS4222:
    index = copyCS4222.index(max(copyCS4222))
    topscoreCS4222list.append(copyNAMES[index])
    copyCS4222[index]= 0

print("CS4141 top scores",topscoreCS4141list) 
print("CS4221 top scores",topscoreCS4222list)
print("CS4222 top scores",topscoreCS4221list)
end=time.time()
time2= ((end-start)*1000)
print(time2)