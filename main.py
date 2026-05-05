import json
import os
from features.show_task import show_task
from features.add_task import add_task

# Konstanta untuk mendefinisikan lokasi file database.
# Semua operasi baca/tulis data pada modul fitur harus mengacu pada file ini.
DB_FILE = 'tasks.json'

def load_tasks():
    # Memeriksa eksistensi file database pada environment lokal.
    # Jika file belum ada, fungsi akan mengembalikan list kosong untuk mencegah error saat parsing.
    if not os.path.exists(DB_FILE):
        return []
    
    # Memuat dan mengembalikan struktur data array dari file JSON.
    with open(DB_FILE, 'r') as file:
        return json.load(file)

def main():
    # Menginisialisasi state aplikasi dengan memuat data dari memori persisten.
    # Referensi list 'tasks' ini yang harus dipassing sebagai argumen ke setiap fungsi fitur.
    tasks = load_tasks()

    while True:
        # Menampilkan antarmuka command-line utama.
        print("\n=== To-Do List App (CLI) ===")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Update Status")
        print("5. Search Task")
        print("6. Exit")

        choice = input("Pilih menu (1-6): ")

        # Blok routing untuk mengarahkan alur eksekusi berdasarkan input pengguna.
        if choice == '1':
            # Memanggil fungsi show_task dari modul eksternal dan mempassing reference list tasks.
            show_task(tasks)
        elif choice == '2':
            # Memanggil fungsi add_task dari modul eksternal dan mempassing reference list tasks.
            add_task(tasks)
        elif choice == '3':
            # TODO: Integrasikan fungsi dari modul Delete Task
            print("Fitur Delete Task belum ditambahkan.")
        elif choice == '4':
            # TODO: Integrasikan fungsi dari modul Update Status
            print("Fitur Update Status belum ditambahkan.")
        elif choice == '5':
            # TODO: Integrasikan fungsi dari modul Search Task
            print("Fitur Search Task belum ditambahkan.")
        elif choice == '6':
            # Menghentikan eksekusi loop utama dan terminasi program.
            print("Keluar dari program...")
            break
        else:
            # Menangani exception logis untuk input pengguna yang berada di luar rentang menu.
            print("Pilihan tidak valid. Silakan pilih angka 1 sampai 6.")

if __name__ == "__main__":
    main()