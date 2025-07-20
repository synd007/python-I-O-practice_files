# Day 1 – Python File Automation Lab

This simple Python script demonstrates basic file and folder manipulation using built-in Python modules. It's part of a hands-on DevOps and automation learning journey.


##  What the Script Does

- Creates a directory called `project_files` (if it doesn't already exist)
- Generates five different files in that directory:
  - Two `.txt` files
  - Two `.log` files
  - One `.tmp` file
- Displays all `.txt` files in the folder
- Moves all `.log` files into a new folder called `log/` in the root directory

- 

##  Tools & Concepts Used

- Python 3
- `os` module for working with directories and paths
- `shutil` module for moving files
- Conditional logic and loops
- Error handling and automation basics

- 


## 🧾 File Structure
project_root/
├── day1.py
├── project_files/
│ ├── readme.txt
│ ├── notes.txt
│ ├── error.log
│ ├── debug.log
│ └── empty.tmp
├── log/
│ ├── error.log
│ └── debug.log
└── README.md
