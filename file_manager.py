import csv
import os

# Field names for the CSV structure
FILE_NAME = 'students.csv' 
FIELDS = ['id', 'name', 'age', 'course', 'status']

def save_to_csv(student_list, FILE_NAME="students.csv"):
    """Saves the list of student dictionaries to a CSV file."""
    try:
        clean_list = [s for s in student_list if s is not None]

        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(clean_list)

        print(f"\n[Success] Data saved to {FILE_NAME} correctly.")
    except PermissionError:
        print("\n[Error] Cannot save: Please close 'students.csvw if it is open.")
    except Exception as e:
        print(f"\n[Error] an unexpected error ocurred while saving {e}")

def load_from_csv(FILE_NAME="students.csv"):
    """Loads student data from a CSV file into a list of dictionaries."""
    student_list = []
    
    if not os.path.exists(FILE_NAME):
        print(f"File {FILE_NAME} not found. A new one will be created upon saving.")
        return student_list
    

    try:
        with open(FILE_NAME, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Ensure age is stored as an integer
                row['age'] = int(row['age'])
                student_list.append(row)
                print(f"Loaded {len(student_list)} studentsmfrom {FILE_NAME}.")
    except Exception as e:
        print(f"Error while loading: {e}")

    return student_list
