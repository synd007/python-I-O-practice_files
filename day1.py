import os
import shutil
cwd = os.getcwd()
print(f"Current Directory: {cwd}")

folder_path = "project_files"

#Using python to create folder #project_files
os.makedirs(folder_path, exist_ok=True)

#Creating five files and writing into them
first_file = os.path.join(folder_path, "readme.txt")
with open(first_file, 'w') as wr:
    wr.write('This is the first file')
second_file = os.path.join(folder_path, "error.log")
with open(second_file, 'w') as wr:
    wr.write('This is the second file')
third_file = os.path.join(folder_path, "notes.txt")
with open(third_file, 'w') as wr:
    wr.write('This is the third file')
fourth_file = os.path.join(folder_path, "debug.log")
with open(fourth_file, 'w') as wr:
    wr.write('This is the fourth file')
fifth_file = os.path.join(folder_path, "empty.tmp")
with open(fifth_file, 'w') as wr:
    wr.write('This is the fifth file')

#print only txt file
txt_file = []
folder_list = os.listdir(folder_path)
for file in folder_list:
    if file.endswith('.txt'):
        txt_file.append(file)
print(f"These are the text files in this folder: {txt_file}")


#Move all .log files into a folder called logs.
#Lets create another folder logs/ in the root directory
dest_dir = os.path.join(cwd, 'log')
os.makedirs(dest_dir, exist_ok=True)
for file in folder_list:
    if file.endswith('.log'):
        source_dir = os.path.join(folder_path, file)
        shutil.move(source_dir , dest_dir)
        print(f"The .log file {file} has been moved to {dest_dir}")


os.makedirs('')