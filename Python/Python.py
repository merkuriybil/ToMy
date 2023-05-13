# ToMy
import os

notes = []

def show_menu():
    print("Note Application")
    print("1. View Notes")
    print("2. Add Note")
    print("3. Delete Note")
    print("4. Exit")

def view_notes():
    if not notes:
        print("No notes available.")
    else:
        print("Notes:")
        for index, note in enumerate(notes):
            print(f"{index + 1}. {note}")

def add_note():
    note = input("Enter your note: ")
    notes.append(note)
    print("Note added successfully.")

def delete_note():
    view_notes()
    if not notes:
        return

    try:
        index = int(input("Enter the index of the note to delete: "))
        if 1 <= index <= len(notes):
            deleted_note = notes.pop(index - 1)
            print(f"Note '{deleted_note}' deleted successfully.")
        else:
            print("Invalid note index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        clear_screen()

        if choice == '1':
            view_notes()
        elif choice == '2':
            add_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == '__main__':
    main()
