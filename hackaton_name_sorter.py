import csv 

csv_file = "C:\Users\conor\OneDrive - University of Limerick\hackaton\cs4222_students_list.csv"


def read_file_to_list(csv_file): 

    lines = [] 

    with open(csv_file, "r") as file: 

        for line in file: 

            lines.append(line.strip()) 

            print(line) 

        return lines 



names= read_file_to_list(csv_file) 

print(names) 


sorted_names= sorted(names, key= lambda x: x.split(",")[1]) 


for entry in sorted_names: 

    print(entry) 
