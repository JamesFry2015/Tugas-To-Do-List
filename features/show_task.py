def show_task(tasks):
    # Menampilkan header untuk membedakan output fitur secara visual pada antarmuka CLI.
    print("\n--- Daftar Task ---")
    
    # Memeriksa apakah struktur data tasks memiliki elemen.
    # Jika kosong, hentikan eksekusi fungsi lebih awal dan berikan feedback ke pengguna.
    if not tasks:
        print("Belum ada task yang terdaftar.")
        return

    # Melakukan iterasi pada struktur data tasks untuk mencetak detail setiap elemen.
    for idx, task in enumerate(tasks, start=1):
        # Memformat representasi status boolean/string menjadi format yang human-readable.
        status = "Selesai" if task.get('status') == 'done' else "Belum"
        
        # Mencetak data task dengan format: [ID]. [Status] Task Name (Assignee).
        print(f"{idx}. [{status}] {task.get('name')} (Assignee: {task.get('assignee')})")