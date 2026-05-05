def search_task(tasks):
    # Meminta input keyword dari pengguna.
    # Kita langsung menggunakan .lower() di sini agar keyword disanitasi menjadi huruf kecil semua,
    # mempermudah perbandingan case-insensitive di tahap filtering.
    keyword = input("\nMasukkan nama assignee yang dicari: ").lower()
    
    # Melakukan filtering menggunakan list comprehension.
    # Kita mengecek apakah substring dari keyword terdapat di dalam value 'assignee'.
    # Value dari 'assignee' juga di-convert ke .lower() sementara (hanya saat evaluasi) agar pencocokannya presisi.
    # Menggunakan .get('assignee', '') untuk menghindari KeyError dan me-return string kosong jika key tidak ada.
    found_tasks = [t for t in tasks if keyword in t.get('assignee', '').lower()]

    # Mencetak header antarmuka untuk hasil pencarian
    print(f"\n--- Hasil Pencarian untuk assignee '{keyword}' ---")
    
    # Mengecek apakah list hasil filter memiliki elemen di dalamnya
    if found_tasks:
        # Melakukan iterasi hanya pada list hasil pencarian (found_tasks), bukan list database utama
        for idx, task in enumerate(found_tasks, start=1):
            # Memformat representasi status boolean/string menjadi format yang lebih rapi untuk CLI
            status = "Selesai" if task.get('status') == 'done' else "Belum"
            
            # Mencetak data task ke terminal.
            # FIX: Menggunakan key 'task' sesuai dengan kesepakatan struktur JSON terbaru,
            # menggantikan key 'name' yang sebelumnya menyebabkan bug output "None".
            print(f"{idx}. [{status}] {task.get('task')} (Assignee: {task.get('assignee')})")
    else:
        # Handling logis jika hasil filter kosong (assignee yang dicari tidak pernah diregistrasi)
        print("Task dengan assignee tersebut tidak ditemukan di dalam database.")
