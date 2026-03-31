# STUDENT MANAGEMENT SYSTEM WITH DATA PERSISTENCE

# PROJECT DESCRIPTION
This program is a console application developed in Python designed for the management of student records. It allows administrative staff to register, view, search, update and delete student information efficiently, ensuring that all data is stored permanently.

# Key Features
**Full CRUD Operations:** Register, consult, search, update and delete students.
**Data Persistence:** Automatically saves and loads student information using a CSV file.
**Input Validation:** Handles basic errors (like invalid ages) to prevent the program crashing.
**Modular Design:** Organized into separate files ('main.py', 'logic.py', 'file_manager.py') for better maintenance.

# Technical Constraints & Architecture
**Language:** Python 3.x.
**Storage:** Data is structured in memory using lists and dictionaries then persisted in a 'students.csv' file.
**Modules:**
*'main.py': Handles the user interface and main menu loop.
*'logic.py': Contains the core functions for data proccessing and input capture.
*'file_manager.py': Manages reading and writing operations to the CSV file.

# How to Run
1. **Ensure Python is installed:** Verify you have Python 3.x on your system.
2. **Download the project:** Save all '.py' files in the same folder.
3. **Open a Terminal:** Navigate to the project directory.
4. **Execute the program:** Run the following command: 
'''bash
python main.py
'''
5. **Usage:** Follow the on-screen menu instructions. Make sure to select the "Save and Exit" option to ensure your changes are written to the file.
