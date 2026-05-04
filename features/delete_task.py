import json

DB_FILE = 'tasks.json'

def delete_task(tasks):
    if not tasks:
        print("Belum ada task yang bisa dihapus.")
        return

    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task.get('task')} - {task.get('assignee')} [{task.get('status')}]")

    try:
        nomor = int(input("Pilih nomor task yang ingin dihapus: "))
        if 1 <= nomor <= len(tasks):
            tasks.pop(nomor - 1)
            
            with open(DB_FILE, 'w') as file:
                json.dump(tasks, file, indent=4)
                
            print("Task berhasil dihapus.")
        else:
            print("Nomor task tidak ditemukan.")
    except ValueError:
        print("Masukkan angka yang valid.")
