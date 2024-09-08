import csv
import time

start= time.time()
csv_file = r"C:\Users\conor\OneDrive - University of Limerick\hackaton\cs4222_students_list.csv"

def read_file_to_list(csv_file):
    lines = []
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)  
        for row in csv_reader:
            lines.append(row)  
    return lines

names = read_file_to_list(csv_file)

sorted_names = sorted(names, key=lambda x: x[1].split(",")[0].strip())  

for entry in sorted_names:
    print(", ".join(entry))  

output_file = r"C:\Users\conor\OneDrive - University of Limerick\hackaton\sorted_students_list.csv"
with open(output_file, "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(sorted_names)

print(f"Sorted names written to '{output_file}' successfully.")


csv_file = r"C:\Users\conor\OneDrive - University of Limerick\hackaton\cs4222_students_list.csv"

def read_file_to_list(csv_file):
    lines = []
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)  
        for row in csv_reader:
            lines.append(row)  
    return lines

names = read_file_to_list(csv_file)

sorted_names = sorted(names, key=lambda x: x[1].split(",")[0].strip())  

for entry in sorted_names:
    print(", ".join(entry))  

output_file = r"C:\Users\conor\OneDrive - University of Limerick\hackaton\sorted_students_list.csv"
with open(output_file, "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(sorted_names)

print(f"Sorted names written to '{output_file}' successfully.")

end=time.time()
time1= ((end-start)*1000)
print(time1)