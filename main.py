# Performance Test - Python Module 1
# Title: Student Management System with Data Persistence

import file_manager
import logic

def main_menu():
 """Main application loop."""
 # Load existing data at startup
 students = file_manager.load_from_csv()

 while True:
    print("\nSTUDENT MANEGEMENT SYSTEM")
    print("1. Register | 2. List | 3. Search | 4. Update | 5. Delete")
    print("6. Save in csv | 7. load into csv | 8. Exit")

    choice = input("Select an option (1-8): ").strip()

    if choice == "1":
        new_student = logic.get_student_input()
        students.append(new_student)
        print("Student added succesfully.")

    elif choice == "2":
        logic.display_students(students)

    elif choice == "3":
       search_id = input("Enter Student ID to search: ").strip()
       # Simple search using a generator expression
       found = next((s for s in students if s and s.get('id') == search_id ), None)
       if found:
          print(f"Result: {found}")
       else:
          print("Students not found.")
       

    elif choice == "4":
       # simple logic to Update
        search_id = input("Enter ID to update: ").strip()
        found_status = False

        for s in students:
          if s and s.get('id') == search_id:
             print(f"Updating data for: {s['name']}")
             
             new_name = input(f"New name ({s['name']}): ").strip()
             new_course = input(f"New course({s['course']}): ").strip()

             s['name'] = new_name or s['name']
             s['course'] = new_course or s['course']
             print("¡Updated!")
             found_status = True
             break
          
          if not found_status:
             print("Student not found.")
             

    elif choice == "5":
       # Simple logic to delete
       search_id = input("Enter ID to delete: ").strip()
       students = [s for s in students if s and s.get('id') != search_id]
       print("Student removed (if it existed). ")

    elif choice == "6":
       file_manager.save_to_csv(students)
       input("\nPress Enter to continue...")
       

    elif choice == "7":
       students = file_manager.load_from_csv()
       
    elif choice == "8":
       print("Saving data and exiting...")
       file_manager.save_to_csv(students)
       print("Goodbye!")
       break

    else:
       print("Option not implemented or invalid. Try again.")

if __name__ =="__main__":
   main_menu()
