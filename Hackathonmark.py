copyCS4222=(CS4222_scores)
copyCS4221 = (CS4221_scores)
copyCS4141 =(CS4141_scores)
copyNAMES =(names)


topscoreCS4221list = []
topscoreCS4222list = []
topscoreCS4141list = []

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