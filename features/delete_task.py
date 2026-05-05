import json
# Mengimpor show_task agar pengguna bisa melihat list sebelum menghapus
from features.show_task import show_task

def delete_task(tasks):
    # Memanggil fitur show_task untuk referensi indeks visual bagi pengguna
    show_task(tasks)
    
    # Jika database kosong, hentikan eksekusi
    if not tasks:
        return

    try:
        choice = int(input("\nMasukkan nomor task yang ingin dihapus: "))
        
        # Validasi batas indeks agar tidak terjadi IndexError
        if 1 <= choice <= len(tasks):
            # Mutasi data: menghapus elemen dari list berdasarkan indeks
            deleted = tasks.pop(choice - 1)
            
            # Persistensi data: menulis ulang state terbaru ke file JSON
            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
                
            # Menggunakan key 'task' sesuai kesepakatan tim (Perbaikan Poin 1)
            print(f"Task '{deleted.get('task')}' berhasil dihapus.")
        else:
            print("Nomor task tidak valid. Data tidak ditemukan.")
    except ValueError:
        # Menangani error jika pengguna memasukkan string/karakter selain angka
        print("Input error: Tolong masukkan format angka yang benar.")
