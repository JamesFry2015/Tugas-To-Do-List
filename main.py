import json
import os
from features.show_task import show_task
from features.add_task import add_task
from features.delete_task import delete_task
from features.update_status import update_status
from features.search_task import search_task

# Konstanta untuk mendefinisikan lokasi file database.
DB_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(DB_FILE):
        return []
    
    with open(DB_FILE, 'r') as file:
        return json.load(file)

def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List App (CLI) ===")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Update Status")
        print("5. Search Task")
        print("6. Exit")

        choice = input("Pilih menu (1-6): ")

        if choice == '1':
            show_task(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            update_status(tasks)
        elif choice == '5':
            search_task(tasks)
        elif choice == '6':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1 sampai 6.")

if __name__ == "__main__":
    main()
