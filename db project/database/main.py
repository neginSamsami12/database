from database_operations import *

def print_menu():
    print('1. Show Employment Questionnaires')
    print('2. Add Employment Questionnaire')
    print('3. Update Employment Questionnaire')
    print('4. Delete Employment Questionnaire')
    print('5. Show Dependents')
    print('6. Add Dependent')
    print('7. Update Dependent')
    print('8. Delete Dependent')
    print('9. Show Employment Questionnaires with Dependents (JOIN)')
    print('10. Show Employment Questionnaires with Male Dependents (LEFT JOIN)')
    print('11. Show Aggregated Employment Questionnaire Data')
    print('12. Quit')

def main():
    while True:
        print_menu()
        choice = input("Select an option (1-12): ")
        if choice == "1":
            select_employment_questionnaires()
        elif choice == "2":
            insert_employment_questionnaire()
        elif choice == "3":
            update_employment_questionnaire()
        elif choice == "4":
            delete_employment_questionnaire()
        elif choice == "5":
            select_dependents()
        elif choice == "6":
            insert_dependent()
        elif choice == "7":
            update_dependent()
        elif choice == "8":
            delete_dependent()
        elif choice == "9":
            select_join_employment_dependents()
        elif choice == "10":
            select_left_join_employment_dependents()
        elif choice == "11":
            select_aggregated_employment_data()
        elif choice == "12":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
from database_operations import *

def print_menu():
    print('1. Show Employment Questionnaires')
    print('2. Add Employment Questionnaire')
    print('3. Update Employment Questionnaire')
    print('4. Delete Employment Questionnaire')
    print('5. Show Dependents')
    print('6. Add Dependent')
    print('7. Update Dependent')
    print('8. Delete Dependent')
    print('9. Show Employment Questionnaires with Dependents (JOIN)')
    print('10. Show Employment Questionnaires with Male Dependents (LEFT JOIN)')
    print('11. Show Aggregated Employment Questionnaire Data')
    print('12. Quit')

def main():
    while True:
        print_menu()
        choice = input("Select an option (1-12): ")
        if choice == "1":
            select_employment_questionnaires()
        elif choice == "2":
            insert_employment_questionnaire()
        elif choice == "3":
            update_employment_questionnaire()
        elif choice == "4":
            delete_employment_questionnaire()
        elif choice == "5":
            select_dependents()
        elif choice == "6":
            insert_dependent()
        elif choice == "7":
            update_dependent()
        elif choice == "8":
            delete_dependent()
        elif choice == "9":
            select_join_employment_dependents()
        elif choice == "10":
            select_left_join_employment_dependents()
        elif choice == "11":
            select_aggregated_employment_data()
        elif choice == "12":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
