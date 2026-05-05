import json

def add_task(tasks):
    # Menampilkan header antarmuka untuk fitur penambahan task.
    print("\n--- Tambah Task Baru ---")
    
    # Mengambil input dari pengguna untuk atribut nama dan assignee.
    name = input("Masukkan nama task: ")
    assignee = input("Masukkan nama assignee: ")

    # Mengkonstruksi objek dictionary baru untuk merepresentasikan task.
    # Atribut status di-hardcode ke 'pending' sebagai state default saat inisialisasi.
    new_task = {
        "name": name,
        "assignee": assignee,
        "status": "pending"
    }
    
    # Melakukan mutasi pada list tasks di memori dengan menambahkan objek baru.
    tasks.append(new_task)

    # Melakukan persistensi data dengan menulis ulang state list tasks terbaru ke dalam file JSON.
    # Parameter indent=4 digunakan untuk memastikan format file tetap human-readable.
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    
    # Memberikan feedback konfirmasi kepada pengguna bahwa operasi I/O dan mutasi memori berhasil.
    print(f"Sistem berhasil meregistrasi task '{name}'.")