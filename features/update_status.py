import json
# Mengimpor show_task agar pengguna dapat melihat referensi ID task
from features.show_task import show_task

def update_status(tasks):
    # Menampilkan daftar task yang ada di memori saat ini
    show_task(tasks)
    
    # Jika struktur data kosong, terminasi fungsi lebih awal
    if not tasks:
        return

    try:
        choice = int(input("\nMasukkan nomor task yang ingin diupdate statusnya: "))
        
        # Validasi batas indeks untuk mencegah IndexError
        if 1 <= choice <= len(tasks):
            # Mendapatkan referensi dictionary task yang dipilih pengguna
            task = tasks[choice - 1]
            
            # Meminta input status baru dan melakukan sanitasi menghapus whitespace berlebih (.strip)
            new_status = input("Masukkan status baru (misal: 'In Progress', 'Done'): ").strip()
            
            # Melakukan mutasi pada atribut status
            task['status'] = new_status
            
            # Persistensi data: menulis ulang state terbaru ke dalam file JSON
            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
                
            # Mencetak log konfirmasi menggunakan key 'task' sesuai standar skema database terbaru
            print(f"Status task '{task.get('task')}' berhasil diubah menjadi '{new_status}'.")
        else:
            print("Nomor task tidak valid. Data tidak ditemukan.")
    except ValueError:
        # Penanganan exception untuk input non-integer pada pemilihan nomor task
        print("Input error: Tolong masukkan format angka yang benar untuk nomor task.")
