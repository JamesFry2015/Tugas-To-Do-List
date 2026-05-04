import json

DB_FILE = 'tasks.json'

def update_status(tasks):
    if not tasks:
        print("Belum ada task yang bisa diupdate.")
        return

    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task.get('task')} - {task.get('assignee')} [{task.get('status')}]")

    try:
        nomor = int(input("Pilih nomor task yang ingin diupdate statusnya: "))
        if 1 <= nomor <= len(tasks):
            status_baru = input("Masukkan status baru (misal: Done, In Progress): ")
            tasks[nomor - 1]['status'] = status_baru
            
            with open(DB_FILE, 'w') as file:
                json.dump(tasks, file, indent=4)
                
            print("Status task berhasil diperbarui.")
        else:
            print("Nomor task tidak ditemukan.")
    except ValueError:
        print("Masukkan angka yang valid.")
