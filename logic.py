def get_student_input():
    """Prompts the user for student details and returns a dictionary."""
    print("\nRegister New Student")

    student_id = input("Enter ID: ").strip()
    name = input("Enter name: ").strip()

    # Basic error handling for age input
    while True:
        age_input = input("Enter Age: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        else:
            print("Invalid input. Please enter a numeric value for age.")

    course = input("Enter Couse/Program: ").strip()
    status = input("Enter Status (Active/Inactive): ").strip()

    return {
        'id': student_id,
        'name': name,
        'age': age,
        'course': course,
        'status': status
            }
        
def display_students(student_list):
    """Prints the list of students in a formatted table."""
    print("\nAccessing Student List")

    if not student_list:
     print("\nNo students found in the system.")
     input("Press Enter to return to the menu...")
     return

    print("\n" + "-" * 80)
    print(f"{'ID':<10} | {'name':<20} | {'age':<5} | {'course':<20} | {'status':<10}")
    print("-" * 80)

    for s in student_list:
        if s:
            s_id = s.get('id', 'N/A')
            s_name = s.get('name', 'N/A')
            s_age = s.get('age', 'N/A')
            s_course = s.get('course', 'N/A')
            s_status = s.get('course', 'N/A')
            print(f"{s_id:<10} | {s_name:<20} | {s_age:<5} | {s_course:<20} | {s_status:<10}")

        print("-" * 80)
        input("\nEnd of list. Press Enter to go back to menu...")
